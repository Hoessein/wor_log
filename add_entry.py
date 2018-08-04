import datetime
import os
import csv

class AddEntry(object):

    def __init__(self):
        pass

    def task_date(self):
        '''Takes an input from the user and makes sure it is in the write format'''
        while True:
            try:
                task_date = input("What is the date of the task? Please use DD/MM/YYYY")
                datetime.datetime.strptime(task_date, '%d/%m/%Y')
                return task_date
            except ValueError:
                print("Please enter a date in the DD/MM/YYYY format")


    def task_title(self):
        '''Takes a task title from the user'''
        task_title = input("What is the title of the task? ")
        return task_title

    def time_spent(self):
        '''Takes an input from the user, the input can only be numbers'''
        while True:
            try:
                time_spent = int(input("How many minutes did you work on it? "))
                return time_spent
            except ValueError:
                print("Please enter the amount of minutes in numbers")

    def notes(self):
        '''Takes additional notes from the user as input'''
        notes = input("Do you have any additional notes? ")
        return notes


    def write_to_csv(self):
        '''writes the data entered by the user to a csv_file'''
        file_exists = os.path.isfile('test.csv')

        with open('test.csv', 'a') as new_file:
            fieldnames = ['TaskDate', 'TaskTitle', 'Minutes', 'Notes']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

            #only if the file does not exist, csv_writer will write the headers
            if not file_exists:
                csv_writer.writeheader()

            csv_writer.writerow({'TaskDate': self.task_date(), 'TaskTitle': self.task_title(),
                                 'Minutes': self.time_spent(), 'Notes': self.notes()})

