import csv
import re
from collections import OrderedDict

class SearchEntry(object):

    def __init__(self):
        self.csv_file = csv.DictReader(open('test.csv', "rt"), delimiter="\t")

    def find_by_date(self):
        find_by_date  = input("enter date")
        for row in self.csv_file:
            if row['TaskDate'] == find_by_date:
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
                      )

    def find_by_time_spent(self):
        find_by_time_spent = input("enter time spent")
        for row in self.csv_file:
            if row['Minutes'] == find_by_time_spent:
                if row['Minutes'] == find_by_time_spent:
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Task title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )

    def find_by_exact_search(self):
        find_by_exact_search = input("Enter your exact search")
        for row in self.csv_file:
            if row['TaskTitle'] or row['Notes'] == find_by_exact_search:
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
                      )

    def find_by_pattern(self):

        find_by_pattern = input(r"Enter your pattern")

        names_file = open("test.csv")
        data = names_file.read()

        pattern = re.findall(find_by_pattern, data)

        print('------------------')
        print('Inside of Pattern: \n', pattern)
        print('------------------')

        for row in self.csv_file:
            for x in pattern:
                if x in row.values():
                    print(row)

        # for row in data:
        #     print(row)
        #
        # for row in self.csv_file:
        #     for x in pik:
        #         if x == row['TaskDate']:
        #             pik2.append(row)
        # print(len(pik2))



            # for field in row:
            #     # if field ==
            #     #     print(row)


                # for x in column:
                #     print(x)
                # "Task title: ", re.search(pattern, row['TaskTitle']).group() + "\n"
                  # "minutes: ", re.search(pattern, row['Minutes']).group() + "\n"
                  # "Notes: ", re.search(pattern, row['Notes']).group() + "\n"


            # print(row['TaskTitle'])
            # print(pattern)
            # match = pattern.match(row['TaskTitle']).groupdict()
            # print(match)
            # # for row in self.csv_file:
            # #     for r in pattern.finditer(row['TaskTitle']):
            # #         print(r)


# some = re.findall(find_by_pattern, row['TaskTitle'])
