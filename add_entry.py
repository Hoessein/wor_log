import datetime


class AddEntry:

    def __init__(self):
        pass

    def task_date(self):
        """Takes an input from the user and makes sure its in the write format"""
        while True:
            try:
                task_date = input("What is the date of the task? Please use DD/MM/YYYY ")
                datetime.datetime.strptime(task_date, '%d/%m/%Y')
                return task_date
            except ValueError:
                print("Please enter a date in the DD/MM/YYYY format ")

    def task_title(self):
        """Takes a task title from the user"""
        task_title = input("What is the title of the task? ")
        return task_title

    def time_spent(self):
        """Takes an input from the user, the input can only be numbers"""
        while True:
            try:
                time_spent = int(input("How many minutes did you work on it? "))
                return time_spent
            except ValueError:
                print("Please enter the amount of minutes in numbers ")

    def notes(self):
        """Takes additional notes from the user as input"""
        notes = input("Do you have any additional notes? ")
        return notes




