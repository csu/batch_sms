import csv
import re

numbers = []
with open(('%s.csv' % filename), 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        if not confirm_col or row[confirm_col] is '1':
            numbers.append(row[phone_col])

pre_filter_count = len(numbers)

numbers = [re.sub("[^0-9]", "", i) for i in numbers]
# not_numbers = [i for i in numbers if not (len(i) < 12 and len(i) > 9)]
# numbers = [i for i in numbers if  (len(i) < 12 and len(i) > 9)]
numbers = ["+1%s" % i for i in numbers if len(i) == 10]

print numbers
# print pre_filter_count
print len(numbers)

with open(('%s.txt' % filename), 'w') as f:
    for i in numbers:
        f.write(i + '\n')