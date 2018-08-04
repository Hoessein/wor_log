import csv
import os.path
import datetime
from add_entry import AddEntry
from search_entry import SearchEntry
import sys


def instructions():
    while True:
        print("WORK LOG")
        some = input("What would you like to do?\n"
                     "a) Add a new entry\n"
                     "b) Search in existing entries\n"
                     "c) Quit program\n")
        if some == 'a':
            add_entry_prompt()
        elif some == 'b':
            search_entry_prompt()
        elif some == 'c':
            break

def add_entry_prompt():
            add_entry.write_to_csv()
            back_to_menu()

def back_to_menu():
        back_to_worklog = input("The entry has been added. Press any key to return to the menu! ")
        if back_to_worklog == "":
            instructions()


def search_entry_prompt():
            #clear
            search_by = input("Do you want to search by: \n"
            "a) Exact date\n"
            "b) Exact search\n" 
            "c) Regex pattern\n"
            "d) Time spent\n"
            "e) return to menu")

            if search_by == 'a':
                search_entry.find_by_date()
            elif search_by == 'b':
                search_entry.find_by_exact_search()
            elif search_by == 'c':
                search_entry.find_by_pattern()
            elif search_by == 'd':
                search_entry.find_by_time_spent()

    # gebruiker moet een invoer kunnen doen en deze moet opgeslagen worden
    # As a user of the script, if I choose to enter a new work log,
    # I should be able to provide a task name, a number of minutes spent working on it,
    # and any additional notes I want to record.
    #the date of the dask: please use DD/MM/YYYY
    #title of the task
    #time spint
    #notes
    #the entry has been add. press enter to return to the menua
    #return to the main menu

    # task_date = input("What is the date of the task? Please use DD/MM/YYYY")
    # try:
    #     datetime.datetime.strptime(task_date, '%d/%m/%Y')
    #     print(task_date)
    # except ValueError:
    #     print("incorrect")
    #
    # task_title = input("What is the title of the task? ")
    #
    # time_spent = input("How many minutes did you work on it? ")
    # try:
    #     pass
    # except ValueError:
    #     pass
    #
    # notes = input("Do you have any additional notes? ")
    #
    # file_exists = os.path.isfile('test.csv')
    #
    # with open('test.csv', 'a') as new_file:
    #     fieldnames = ['TaskDate', 'TaskTitle', 'Minutes', 'Notes']
    #
    #     csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
    #
    #     if not file_exists:
    #         csv_writer.writeheader()
    #
    #     csv_writer.writerow({'TaskDate': task_date, 'TaskTitle': task_title, 'Minutes': time_spent, 'Notes': notes})
    #
    # print("The entry has been added. Press enter to return to the menu! ")
    # # #
    # # # if some == 'b':
    # # #     # gebruiker moet kunnen zoeken naar een taak
    # #     pass
    # #
    # # if some == 'c':
    # #     # moet het programma worden gestopt
    # #     pass
    # #
    #

search_entry = SearchEntry()
add_entry = AddEntry()

if __name__ == '__main__':
    instructions()