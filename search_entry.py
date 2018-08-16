import csv
import re
import datetime
import os


class SearchEntry:

    def __init__(self):
        # couple of instance variables I need
        self.dates = []
        self.minutes = []
        self.exact = []
        self.exact_search = ""
        self.pattern = []
        self.pattern_search = ""
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

    def open_update_csv(self):
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')
            return self.reader

    def printer(self, search_by_string, rowname1, rowname2):
        entries_counter = 1
        print("Here are the entries for:", search_by_string, "\n")

        for row in self.reader:
            if row[rowname1] == str(search_by_string):
                print("Entry:", entries_counter)
                print("Task date: " + row['Taskdate'] + "\n"
                      "Task title: " + row['Tasktitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes']
                      )
                print("_________")
                entries_counter += 1

    def if_no(self, search, search1, method):
        print("There are no entries with: " + search)
        while True:
            try_again = input("\nEnter 1 to try another {}"
                              "\nEnter 2 to go back to the menu!\n".format(search1))
            if try_again == '1':
                self.clear()
                method()
                break
            elif try_again == '2':
                break
            # the loop will keep running if they don't pick 1 to try again
            # or 2 to go back to the menu
            else:
                self.clear()
                print("Pick one of the provided options")
                continue

    def date_entries(self):
        """This method prints all of the entries to the screen
        which the user can then pick from"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            counter = 1

            # all of the entries are appeneded to a list stored in an instance variable
            for row in self.reader:
                if row['Taskdate']:
                    self.dates.append(row['Taskdate'])

            if len(self.dates) > 0:
                print("You can pick from the following: \n")

            for x in set(self.dates):
                print(str(counter) + ': ' + x)
                counter += 1

    def find_by_date(self):
        """The user is asked to input a date from the options printed to the screen
           The user is then shown a corresponding work log entry"""
        while True:
            try:
                find_by_date = input("\nWhat is the date of the task? Please use DD/MM/YYYY ")
                # the input must be in a specific date format, otherwise it won't be accepted.
                datetime.datetime.strptime(find_by_date, '%d/%m/%Y')
                self.clear()
                # if the entry is available it will break out of the loop
                if find_by_date in set(self.dates):
                    self.printer(find_by_date, "Taskdate", rowname2=None)
                    break
                # if the entry is not available the user is asked to try again
                else:
                    print("There are no entries with: " + find_by_date + " try again!\n")
                    self.date_entries()
            except ValueError:
                self.clear()
                print("Please enter a date in the DD/MM/YYYY format!\n")
                self.date_entries()

    def time_entries(self):
        """This method prints all of the entries to the screen
        which the user can pick from"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            counter = 1

            # all of the entries are appeneded to a list stored in an instance variable
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
                # if the entry is available it will break out of the loop
                if find_by_time_spent in set(self.minutes):
                    self.printer(find_by_time_spent, "Minutes", rowname2=None)
                    break
                # if the entry is not available the user is asked to try again
                else:
                    print("There are no entries with: " + str(find_by_time_spent) + " minutes, try again!\n")
                    self.time_entries()
            except ValueError:
                self.clear()
                print("Please enter the amount of minutes in numbers")
                self.time_entries()

    def exact_entries(self):
        """This method prints all of the entries to the screen
        which the user can pick from"""
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            # all of the entries are appeneded to a list stored in an instance variable
            for row in self.reader:
                if row['Tasktitle']:
                    self.exact.append(row['Tasktitle'])
                if row['Notes']:
                    self.exact.append(row['Notes'])

    def no_exact_filter(self):
        """This method filters if the exact search of the user exists"""
        while True:
            self.exact_search = input("What is your exact search? ").lower()
            self.clear()
            # if the entry is available it will break out of the loop
            for x in set(self.exact):
                if self.exact_search == x:
                    self.printer(self.exact_search, "Tasktitle", "Notes")
                    return
            # if the entry is not available the user is asked to try again
            else:
                self.if_no(self.exact_search, "exact search", self.no_exact_filter)
                # if the input doesn't exist in the worklog,
                # the user is told to try again or can return to the menu
                return

    def make_data(self):
        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()
            self.reader = csv.DictReader(csv_file, delimiter='\t')
            names_file = open("worklog.csv")
            next(csv_file)
            data = names_file.read()
            return data

    def match_filter(self):
        """This method checks if the entry of the regex contains a match"""
        while True:
            self.pattern_search = input(r"Enter your regex pattern: ")
            if re.match(self.pattern_search, self.make_data()) and self.pattern_search != "":
                self.no_pattern_filter()
                break
            else:
                self.if_no(self.pattern_search, "regex pattern", self.match_filter)
                break

    def no_pattern_filter(self):
        """This method filters if the regex pattern search of the user exists"""
        while True:
            with open('worklog.csv', 'r') as csv_file:
                self.update_csv()

                self.reader = csv.DictReader(csv_file, delimiter='\t')

                self.clear()

                names_file = open("worklog.csv")
                data = names_file.read()

                self.pattern = re.findall(self.pattern_search, data)
                print(self.pattern)

                for row in self.reader:
                    for x in set(self.pattern):
                        print(x)
                        # if the entry matches anything it will break out of the loop
                        if x in row['Tasktitle'] or x in row['Notes']:
                            self.find_by_pattern()
                            return

    def find_by_pattern(self):
        """A regex input is expected, this method checks if there is a match and prints it out"""

        with open('worklog.csv', 'r') as csv_file:
            self.update_csv()

            self.reader = csv.DictReader(csv_file, delimiter='\t')

            self.clear()
            names_file = open("worklog.csv")
            data = names_file.read()
            print(re.match(self.pattern_search, data))

            entries_counter = 1

            print("Here are all task title and or note entries for " + self.pattern_search + ":\n")


            for row in self.reader:
                for x in set(self.pattern):
                    # The regex pattern is based on the columns: 'Tasktitle' and 'Notes'
                    if x in row['Tasktitle'] or x in row['Notes']:
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
