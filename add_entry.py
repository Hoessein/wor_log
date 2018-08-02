import datetime
import os
import csv

class AddEntry(object):

    def __init__(self):
        pass

    def task_date(self):
        while True:
            try:
                task_date = input("What is the date of the task? Please use DD/MM/YYYY")
                datetime.datetime.strptime(task_date, '%d/%m/%Y')
                return task_date
            except ValueError:
                print("Please enter a date in the DD/MM/YYYY format")

    def task_title(self):
        task_title = input("What is the title of the task? ")
        return task_title

    def time_spent(self):
        while True:
            try:
                time_spent = int(input("How many minutes did you work on it? "))
                return time_spent
            except ValueError:
                print("Please enter the amount of minutes in numbers")

    def notes(self):
        notes = input("Do you have any additional notes? ")
        return notes


    def write_to_csv(self):
        file_exists = os.path.isfile('test.csv')

        with open('test.csv', 'a') as new_file:
            fieldnames = ['TaskDate', 'TaskTitle', 'Minutes', 'Notes']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

            if not file_exists:
                csv_writer.writeheader()

            csv_writer.writerow({'TaskDate': add_entry.task_date(), 'TaskTitle': add_entry.task_title(),
                                 'Minutes': add_entry.time_spent(), 'Notes': add_entry.notes()})


add_entry = AddEntry()
add_entry.write_to_csv()