import csv
import re


class SearchEntry(object):

    def __init__(self):
        self.csv_file = csv.DictReader(open('test.csv', "rt"), delimiter="\t")

    def find_by_date(self):
        """The user is asked to input a date.
           The user is then shown a corresponding work log entry"""

        find_by_date  = input("enter date")
        for row in self.csv_file:
            if row['TaskDate'] == find_by_date:
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
                      )

    def find_by_time_spent(self):
        """The user is asked to input a number of minutes.
            The user is then showed a work log entry corresponding
            the entered minutes"""

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
        """The user is asked to input a search criteria
            and prints out corresponding work log entries"""

        find_by_exact_search = input("Enter your exact search")
        for row in self.csv_file:
            # The exact search is based on the columns: 'TaskTitle' and 'Notes'
            if row['TaskTitle'] == find_by_exact_search:
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
            )

        for row in self.csv_file:
            # The exact search is based on the columns: 'TaskTitle' and 'Notes'
            if row['Notes'] == find_by_exact_search:
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
                      )

    def find_by_pattern(self):
        """A regex input is expected, this method check if there is a match and prints it out"""
        find_by_pattern = input(r"Enter your pattern")

        names_file = open("test.csv")
        data = names_file.read()

        pattern = re.findall(find_by_pattern, data)

        print(set(pattern))

        for row in self.csv_file:
            for x in set(pattern):

                if x in row['TaskTitle']:
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Tas title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )

                if x in row['Notes']:
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Task title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
