import csv
import re

confirm_col = 3
phone_col = 8
numbers = []
with open('confirmations.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        if row[confirm_col] is '1':
            numbers.append(row[phone_col])

pre_filter_count = len(numbers)

numbers = [re.sub("[^0-9]", "", i) for i in numbers]
# not_numbers = [i for i in numbers if not (len(i) < 12 and len(i) > 9)]
# numbers = [i for i in numbers if  (len(i) < 12 and len(i) > 9)]
numbers = ["+1%s" % i for i in numbers if len(i) == 10]

print numbers
# print pre_filter_count
print len(numbers)