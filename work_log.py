import csv
import os.path
import datetime
from add_entry import AddEntry
from search_entry import SearchEntry
import sys

file_exists = os.path.isfile('morg.csv')

def instructions():
    """Instructions on how the console works
    it accepts a user input"""
    while True:
        print("WORK LOG")
        some = input("What would you like to do?\n"
                     "a) Add a new entry\n"
                     "b) Search in existing entries\n"
                     "c) Quit program\n")
        if some == 'a':
            clear()
            add_entry_prompt()
        elif some == 'b':
            if file_exists:
                clear()
                search_entry_prompt()
            else:
                print("There are no entries, first add an entry before you can search")
        elif some == 'c':
            clear()
            print("Thank you for using the Worklog, goodbye!")
            sys.exit()

def clear():
    """This is a function that clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def add_entry_prompt():
    """Creates a csv file, in the csv method the methods to ask user for input will be called
        After the entry is added, theinstructions menu will be shown again"""
    add_entry.write_to_csv()
    back_to_menu()

def back_to_menu():
    """If the user enters any key they will be taken back to the menu"""
    back_to_menu = input("The entry has been added. Press any key to return to the menu! ")
    if back_to_menu == "":
        clear()
        instructions()


def search_entry_prompt():
        #clear
        """The search method will be run accordingly depending on the user input"""
        search_by = input("Do you want to search by: \n"
        "a) Exact date\n"
        "b) Exact search\n" 
        "c) Regex pattern\n"
        "d) Time spent\n"
        "e) return to menu")

        if search_by == 'a':
            clear()
            search_entry.find_by_date()
        elif search_by == 'b':
            clear()
            search_entry.find_by_exact_search()
        elif search_by == 'c':
            clear()
            search_entry.find_by_pattern()
        elif search_by == 'd':
            clear()
            search_entry.find_by_time_spent()

#couple of instances
search_entry = SearchEntry()
add_entry = AddEntry()

if __name__ == '__main__':
    instructions()