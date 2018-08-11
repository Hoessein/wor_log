import csv
import re
import os


class SearchEntry():

    def __init__(self):

        file_exists = os.path.isfile('worklog.csv')

        if file_exists:
            self.reader = self.update_csv()

    def update_csv(self):
        with open('worklog.csv', 'r') as csv_file:
            self.reader = csv.DictReader(csv_file, delimiter='\t')

    def clear(self):
        """This is a function that clears the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def find_by_date(self):
        """The user is asked to input a date.
           The user is then shown a corresponding work log entry"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            find_by_date = input("Enter a date")

            for row in self.reader:
                if row['Taskdate'] in find_by_date:
                    self.clear()
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
            else:
                self.clear()
                print("There are no matches found, try again please hihihihi")


    def find_by_time_spent(self):
        """The user is asked to input a number of minutes.
            The user is then showed a work log entry corresponding
            the entered minutes"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            find_by_time_spent = input("Enter minutes")
            for row in self.reader:
                if row['Minutes'] == find_by_time_spent:
                    self.clear()
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
            else:
                self.clear()
                print("There are no matches found, try again please")

    def find_by_exact_search(self):
        """The user is asked to input a search criteria
            and prints out corresponding work log entries"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            exact_search = input("Enter your exact search")

            for row in self.reader:
                #The exact search is based on the columns: 'Tasktitle' and 'Notes'
                if row['Tasktitle'] in exact_search or row['Notes'] in exact_search:
                    self.clear()
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )

            else:
                self.clear()
                print("There are no matches found, try again please")

    def find_by_pattern(self):
        """A regex input is expected, this method check if there is a match and prints it out"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            find_by_pattern = input(r"Enter your pattern")

            names_file = open("worklog.csv")
            data = names_file.read()

            pattern = re.findall(find_by_pattern, data)

            names_file.close()

            for row in self.reader:
                for x in set(pattern):

                    if x in row['Tasktitle'] or x in row['Notes']:
                        print("Task date: " + row['Taskdate'] + "\n"
                              "Task title: " + row['Tasktitle'] + "\n"
                              "Minutes: " + row['Minutes'] + "\n"
                              "Notes: " + row['Notes'] + "\n"
                              )
                        break
                else:
                    self.clear()
                    print("There are no matches found, try again please")
                    break
