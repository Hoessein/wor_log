import csv
import re
import datetime
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

    def date_entries(self):
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            counter = 1
            for row in self.reader:
                if row['Taskdate']:
                    print(str(counter)+','+ row['Taskdate'])
                    counter += 1

    def find_by_date(self):
        """The user is asked to input a date.
           The user is then shown a corresponding work log entry"""

        while True:
            try:
                find_by_date = input("What is the date of the task? Please use DD/MM/YYYY")
                datetime.datetime.strptime(find_by_date, '%d/%m/%Y')
                break
            except ValueError:
                print("Please enter a date in the DD/MM/YYYY format")
                self.clear()
                self.date_entries()

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            self.entries_counter = 0

            for row in self.reader:
                if row['Taskdate'] == find_by_date:
                    self.clear()
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
                    self.entries_counter += 1

            if self.entries_counter == 0:
                self.clear()
                print("There are no matches found, try again please")


    def time_entries(self):
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            counter = 1
            for row in self.reader:
                if row['Minutes']:
                    print(str(counter) + ":", row['Minutes'] + " minutes")
                    counter += 1

    def find_by_time_spent(self):
        """The user is asked to input a number of minutes.
            The user is then showed a work log entry corresponding
            the entered minutes"""

        while True:
            try:
                find_by_time_spent = int(input("How many minutes did you work on it? "))
                break
            except ValueError:
                self.clear()
                print("Please enter the amount of minutes in numbers")
                self.time_entries()

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            self.entries_counter = 0

            for row in self.reader:
                if row['Minutes'] == str(find_by_time_spent):
                    self.clear()
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
                    self.entries_counter += 1

            if self.entries_counter == 0:
                self.clear()
                print("There are no matches found, try again please")


    def find_by_exact_search(self):
        """The user is asked to input a search criteria
            and prints out corresponding work log entries"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            exact_search = input("Enter your exact search")

            self.entries_counter = 0

            for row in self.reader:
                #The exact search is based on the columns: 'Tasktitle' and 'Notes'
                if row['Tasktitle'] == exact_search or row['Notes'] == exact_search:
                    self.clear()
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
                    self.entries_counter += 1

            if self.entries_counter == 0:
                self.clear()
                print("There are no matches found, try again please")

    def find_by_pattern(self):
        """A regex input is expected, this method check if there is a match and prints it out"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter ='\t')

            find_by_pattern = input(r"Enter your pattern")

            self.entries_counter = 0

            names_file = open("worklog.csv")
            data = names_file.read()

            pattern = re.findall(find_by_pattern, data)

            names_file.close()

            for row in self.reader:
                for x in set(pattern):


                    if x == row['Tasktitle'] or x == row['Notes']:
                        print("Task date: " + row['Taskdate'] + "\n"
                              "Task title: " + row['Tasktitle'] + "\n"
                              "Minutes: " + row['Minutes'] + "\n"
                              "Notes: " + row['Notes'] + "\n"
                              )
                        self.entries_counter += 1
                        break

            if self.entries_counter == 0:
                self.clear()
                print("There are no matches found, try again please")

