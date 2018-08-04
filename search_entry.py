import csv
import re


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
                          "Miutes: " + row['Minutes'] + "\n"
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

        for row in self.csv_file:
            for x in set(pattern):

                if x in row.values():
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Task title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )