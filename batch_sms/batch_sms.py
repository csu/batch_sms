# Batch SMS
# Christopher J. Su
# Copyright (c) 2015

import dataset
from sqlalchemy import String

class BatchSMS:
  def __init__(self, db_file, batch_sender, auto_associate=False):
    self.db = dataset.connect('sqlite:///%s' % db_file)
    self.batch_sender = batch_sender
    self.auto_associate = auto_associate

    # prepare db
    self.from_numbers = self.db.get_table('from_numbers', primary_id='number', primary_type='String')
    self.to_numbers = self.db.get_table('to_numbers', primary_id='number', primary_type='String')
    self.associations = self.db.get_table('associations', primary_id='to_num', primary_type='String')
    self.subscription_lists = self.db.get_table('subscription_lists', primary_id='name', primary_type='String')
    self.subscriptions = self.db.get_table('subscriptions')

    self.associations.create_column('from_num', String)

  # From Numbers
  def add_from_number(self, from_num):
    self.from_numbers.upsert(dict(number=from_num), ['number'])

  def remove_from_number(self, from_num):
    self.from_numbers.delete(number=from_num)

  # To Numbers
  def add_to_number(self, to_num, subs=None):
    self.to_numbers.upsert(dict(number=to_num), ['number'])

    # If auto association is enabled, we will automatically
    # assign new to numbers to the from number with the
    # fewest associations.
    # This could be further optimized for consecutive adds.
    if self.auto_associate:
      min_from_num = self.from_num_with_fewest_associations()
      self.associate(to_num, min_from_num)

    if subs:
      for sub_id in subs:
        self.add_to_subscription(to_num, sub_id)

  def remove_to_number(self, to_num):
    self.to_numbers.delete(number=to_num)

  # Associations
  def associate(self, to_num, from_num):
    # these should both be foreign keys, but too lazy to use ORM
    self.associations.upsert(dict(to_num=to_num, from_num=from_num), ['to_num'])

  def from_num_associations(self):
    return self.db.query('SELECT from_num, COUNT(*) c FROM associations GROUP BY from_num')

  def from_num_with_fewest_associations(self):
    res = self.db.query('''SELECT number, min(c)
      FROM (SELECT number, COUNT(to_num) c
        FROM from_numbers
        LEFT OUTER JOIN associations
        ON from_numbers.number = associations.from_num
        GROUP BY number)''')
    for row in res:
      return row['number']

  @staticmethod
  def min_from_num_in_associations(associations, count_key):
    """
    Returns the dict for the association in associations,
    a list of associations as dicts, with the lowest value
    for count_key.
    """
    return min(associations, key=lambda x:x[count_key])

  # Subscription Lists
  def create_subscription_list(self, name):
    return self.subscription_lists.insert({'name': name})

  def update_subscription_list(self, subscription_id, name):
    self.subscription_lists.update({'id': subscription_id, 'name': name}, ['id'])

  def get_subscription_lists_by_name(self, name):
    sub_id = self.subscription_lists.find(name=name)
    for row in sub_id:
      return row['id']
    return None

  def get_or_create_subscription_list(self, name):
    existing = self.get_subscription_lists_by_name(name)
    if existing:
      return existing
    return self.create_subscription_list(name)

  def delete_subscription_list(self, subscription_id):
    """
    Deletes a subscription list and all subscriptions for it.
    """
    pass

  # Subscriptions
  def add_to_subscription(self, to_num, subscription_id):
    if isinstance(to_num, list):
      for n in to_num:
        self.subscriptions.insert({'to_num': n, 'subscription': subscription_id})

    # Subscription should be a foreign key,
    # but I'm too lazy to use a full-blown ORM for this
    self.subscriptions.insert({'to_num': to_num, 'subscription': subscription_id})

  # Message sending
  def send_to_subscription(self, subscription_id, message_body, callback=None, on_fail=None):
    to_nums = self.subscriptions.find(subscription=subscription_id)
    sub_list_nums = {}
    for to_num in to_nums:
      association = self.associations.find_one(to_num=to_num['to_num'])
      if association is None:
        raise ValueError('No association found for ' + to_num['to_num'])
      from_num = association['from_num']
      if not from_num in sub_list_nums:
        sub_list_nums[from_num] = set()
      sub_list_nums[from_num].add(to_num['to_num'])
    self.batch_sender.send_sms(message_body, sub_list_nums, callback=callback, on_fail=on_fail)

  def send_to_subscriptions(self, sub_ids, message_body, callback=None, on_fail=None):
    to_nums = set()
    for sub_id in sub_ids:
      sub_nums = self.subscriptions.find(subscription=sub_id)
      for num in sub_nums:
        to_nums.add(num['to_num'])

    sub_list_nums = {}
    for to_num in to_nums:
      association = self.associations.find_one(to_num=to_num)
      if association is None:
        raise ValueError('No association found for ' + to_num)
      from_num = association['from_num']
      if not from_num in sub_list_nums:
        sub_list_nums[from_num] = set()
      sub_list_nums[from_num].add(to_num)
      
    self.batch_sender.send_sms(message_body, sub_list_nums, callback=callback, on_fail=on_fail)