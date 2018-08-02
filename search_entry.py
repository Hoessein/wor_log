import csv
import re

class SearchEntry(object):

    def __init__(self):
        self.csv_file = csv.DictReader(open('test.csv', "rt"), delimiter="\t")

    def find_by_date(self):
        find_by_date  = input("enter date")
        for row in self.csv_file:
            if row['TaskDate'] == find_by_date:
                print(row, "heyyy")

    def find_by_time_spent(self):
        find_by_time_spent = input("enter time spent")
        for row in self.csv_file:
            if row['Minutes'] == find_by_time_spent:
                print(row)

    def find_by_exact_search(self):
        find_by_exact_search = input("Enter your exact search")
        for row in self.csv_file:
            if row['TaskTitle'] or row['Notes'] == find_by_exact_search:
                print(row)

    def find_by_pattern(self):

        find_by_pattern = input(r"Enter your pattern")
        pattern = re.compile(find_by_pattern)

        for row in self.csv_file:
            print(re.search(pattern, row['TaskDate']).group())
            print(row)

            # print(row['TaskTitle'])
            # print(pattern)
            # match = pattern.match(row['TaskTitle']).groupdict()
            # print(match)
            # # for row in self.csv_file:
            # #     for r in pattern.finditer(row['TaskTitle']):
            # #         print(r)


# some = re.findall(find_by_pattern, row['TaskTitle'])
