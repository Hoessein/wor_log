import csv
import re
import datetime
import os


class SearchEntry:

    def __init__(self):
        self.dates = []
        self.minutes = []
        self.exact = []
        file_exists = os.path.isfile('worklog.csv')

        if file_exists:
            self.reader = self.update_csv()

    def update_csv(self):
        """This is a helper method used in the init
        to update the latest entries to the csv_file"""
        with open('worklog.csv', 'r') as csv_file:
            self.reader = csv.DictReader(csv_file, delimiter='\t')

    def clear(self):
        """This is a method that clears the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def date_entries(self):
        """This method prints all of the entries to the screen
        which the user can pick from"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            counter = 1

            for row in self.reader:
                if row['Taskdate']:
                    self.dates.append(row['Taskdate'])

            if len(self.dates) > 0:
                print("You can pick from the following: \n")

            for x in set(self.dates):
                print(str(counter) + ': ' + x)
                counter += 1


    def find_by_date(self):
        """The user is asked to input a date.
           The user is then shown a corresponding work log entry"""

        while True:
            try:
                find_by_date = input("\nWhat is the date of the task? Please use DD/MM/YYYY ")
                datetime.datetime.strptime(find_by_date, '%d/%m/%Y')
                self.clear()
                if find_by_date in set(self.dates):
                    break
                else:
                    print("\There are no entries with: " + find_by_date + " try again!\n")
                    self.date_entries()
            except ValueError:
                self.clear()
                print("Please enter a date in the DD/MM/YYYY format!\n")
                self.date_entries()

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            entries_counter = 1
            print("Here are the entries for:", find_by_date, "\n")

            for row in self.reader:
                if row['Taskdate'] == str(find_by_date):
                    print("Entry:", entries_counter)
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes']
                          )
                    print("_________")
                    entries_counter += 1

            if entries_counter == 1:
                self.clear()
                print("There are no matches found for: " + find_by_date + ", try again")

    def time_entries(self):
        """This method prints all of the entries to the screen
        which the user can pick from"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            counter = 1

            for row in self.reader:
                if row['Minutes']:
                    self.minutes.append(row['Minutes'])
            if len(self.minutes) > 0:
                print("You can pick from the following: \n")

            for x in set(self.minutes):
                print(str(counter) + ': ' + x + ' minutes')
                counter += 1

    def find_by_time_spent(self):
        """The user is asked to input a number of minutes.
            The user is then showed a work log entry corresponding
            the entered minutes"""

        while True:
            try:
                find_by_time_spent = input("\nWhat are the minutes spent on the task? "
                                           "Please enter the amount of minutes in numbers only ")
                self.clear()
                if find_by_time_spent in set(self.minutes):
                    break
                else:
                    print("There are no entries with: " + str(find_by_time_spent) + " minutes, try again!\n")
                    self.time_entries()
            except ValueError:
                self.clear()
                print("Please enter the amount of minutes in numbers")
                self.time_entries()

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            entries_counter = 1
            print("Here are the entries for", find_by_time_spent, "minutes: \n")

            for row in self.reader:
                if row['Minutes'] == str(find_by_time_spent):
                    print("Entry:", entries_counter)
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes']
                          )
                    print("_________")
                    entries_counter += 1

            if entries_counter == 1:
                self.clear()
                print("There are no matches found, try again please")

    def exact_entries(self):
        """This method prints all of the entries to the screen
        which the user can pick from"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            counter = 1

            for row in self.reader:
                if row['Tasktitle']:
                    self.exact.append(row['Tasktitle'])
                if row['Notes']:
                    self.exact.append(row['Notes'])
            if len(self.exact) > 0:
                print("You can pick from the following: \n")

            for x in set(self.exact):
                print(str(counter) + ': ' + x)
                counter += 1

    def find_by_exact_search(self):
        """The user is asked to input a search criteria
            and prints out corresponding work log entries"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            exact_search = input("What is your exact search? ")
            self.clear()

            entries_counter = 1
            print("Here are all task title and or note entries for " + exact_search + ":\n")

            for row in self.reader:

                # The exact search is based on the columns: 'Tasktitle' and 'Notes'
                if row['Tasktitle'] == exact_search or row['Notes'] == exact_search:
                    print("Entry:", entries_counter)
                    print("Task date: " + row['Taskdate'] + "\n"
                          "Task title: " + row['Tasktitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes']
                          )
                    print("_________")
                    entries_counter += 1

            if entries_counter == 1:
                self.clear()
                print("There are no matches found, try again please")

    def find_by_pattern(self):
        """A regex input is expected, this method checks if there is a match and prints it out"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            find_by_pattern = input(r"Enter your regex pattern ")
            self.clear()

            entries_counter = 1
            print("Here are all task title and or note entries for " + find_by_pattern + ":\n")


            names_file = open("worklog.csv")
            data = names_file.read()

            pattern = re.findall(find_by_pattern, data)

            names_file.close()

            for row in self.reader:
                for x in set(pattern):

                    if x == row['Tasktitle'] or x == row['Notes']:
                        print("Entry:", entries_counter)
                        print("Task date: " + row['Taskdate'] + "\n"
                              "Task title: " + row['Tasktitle'] + "\n"
                              "Minutes: " + row['Minutes'] + "\n"
                              "Notes: " + row['Notes'] + "\n"
                              )
                        print("_________")
                        entries_counter += 1
                        break

            if entries_counter == 1:
                self.clear()
                print("There are no matches found, try again please")
