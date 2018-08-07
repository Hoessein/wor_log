import csv
import re
import os


class SearchEntry(object):

    def __init__(self):

        file_exists = os.path.isfile('morg.csv')

        if file_exists:
            self.csv_file = csv.DictReader(open('morg.csv', "rt"), delimiter="\t")

    def clear(self):
        """This is a function that clears the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def find_by_date(self):
        """The user is asked to input a date.
           The user is then shown a corresponding work log entry"""

        find_by_date = input("Enter a date")
        print("im outside the for loop")
        for row in self.csv_file:
            print("i'm inside the for loop")
            if row['TaskDate'] == find_by_date:
                self.clear()
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
                      )
                    self.csv_file.seek()
            else:
                self.clear()
                print("There are no matches found, try again please")


    def find_by_time_spent(self):
        """The user is asked to input a number of minutes.
            The user is then showed a work log entry corresponding
            the entered minutes"""

        find_by_time_spent = input("Enter minutes")
        for row in self.csv_file:
            if row['Minutes'] == find_by_time_spent:
                    self.clear()
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Task title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
            else:
                self.clear()
                print("There are no matches found, try again please")

    def find_by_exact_search(self):
        """The user is asked to input a search criteria
            and prints out corresponding work log entries"""

        exact_search = input("Enter your exact search")
        for row in self.csv_file:
            # The exact search is based on the columns: 'TaskTitle' and 'Notes'
            if exact_search in row['TaskTitle'] or row['Notes']:
                self.clear()
                print("Task date: " + row['TaskDate'] + "\n"
                      "Task title: " + row['TaskTitle'] + "\n"
                      "Minutes: " + row['Minutes'] + "\n"
                      "Notes: " + row['Notes'] + "\n"
                      )
            else:
                self.clear()
                print("There are no matches found, try again please")

    def find_by_pattern(self):
        """A regex input is expected, this method check if there is a match and prints it out"""
        find_by_pattern = input(r"Enter your pattern")

        names_file = open("morg.csv")
        data = names_file.read()

        pattern = re.findall(find_by_pattern, data)

        names_file.close()

        for row in self.csv_file:
            for x in set(pattern):

                if x in row['TaskTitle']:
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Task title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
                    break

                if x in row['Notes']:
                    print("Task date: " + row['TaskDate'] + "\n"
                          "Task title: " + row['TaskTitle'] + "\n"
                          "Minutes: " + row['Minutes'] + "\n"
                          "Notes: " + row['Notes'] + "\n"
                          )
                    break
            else:
                self.clear()
                print("There are no matches found, try again please")

