import os.path
from add_entry import AddEntry
from search_entry import SearchEntry
import sys
import csv

# couple of instances
add_entry = AddEntry()
search_entry = SearchEntry()


def instructions():
    """Instructions on how the console works
    it accepts a user input"""
    search_entry.clear()

    while True:
        print("WORK LOG \n"
              "Press a to add a new entry \n"
              "Press b to search in existing entries\n"
              "Press c to quit the program\n"
              )

        start = input("What would you like to do? ").lower()

        if start == 'a':
            search_entry.clear()
            add_entry_prompt()
        elif start == 'b':
            # if the file doesn't exist it means that there are no entries made so a search is not possible
            file_exists = os.path.isfile('worklog.csv')
            if file_exists:
                search_entry.clear()
                search_entry_prompt()
            else:
                search_entry.clear()
                print("There are no entries made in the work log, first add an entry before you search!\n")

        elif start == 'c':
            search_entry.clear()
            print("Thank you for using the Worklog, goodbye!")
            sys.exit()

        else:
            search_entry.clear()


def add_entry_prompt():
    """Creates a csv file, in the csv method the methods to ask user for input will be called
        After the entry is added, the instructions menu will be shown again"""
    write_to_csv()
    back_to_menu()


def back_to_menu():
    """If the user enters any key they will be taken back to the menu"""
    to_menu = input("\nThe entry has been added. Press any key to return to the menu! ")
    search_entry.clear()

    if to_menu == "":
        search_entry.clear()
        instructions()


def search_entry_prompt():
    """The search method will be run accordingly depending on the user input"""
    search_by = input("Do you want to search by: \n\n"
                      "a) Exact date\n"
                      "b) Exact search\n" 
                      "c) Regex pattern\n"
                      "d) Time spent\n"
                      "e) return to menu ").lower()
    if search_by == 'a':
        search_entry.clear()
        search_entry.date_entries()
        search_entry.find_by_date()
    elif search_by == 'b':
        search_entry.clear()
        search_entry.exact_entries()
        search_entry.no_exact_filter()
        search_entry.find_by_exact_search()
    elif search_by == 'c':
        search_entry.clear()
        search_entry.no_pattern_filter()
        search_entry.find_by_pattern()
    elif search_by == 'd':
        search_entry.clear()
        search_entry.time_entries()
        search_entry.find_by_time_spent()
    elif search_by == 'e':
        instructions()
    else:
        search_entry.clear()
        print("Please pick an option from the provided list.\n")
        search_entry_prompt()


def write_to_csv():
    """writes entries to the csv file"""
    file_exists = os.path.isfile('worklog.csv')

    with open('worklog.csv', 'a') as csv_file:
        fieldnames = ['Taskdate', 'Tasktitle', 'Minutes', 'Notes']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')

        # only if the file does not exist, csv_writer will write the headers
        if not file_exists:
            csv_writer.writeheader()

        csv_writer.writerow({'Taskdate': add_entry.task_date(), 'Tasktitle': add_entry.task_title(),
                             'Minutes': add_entry.time_spent(), 'Notes': add_entry.notes()})

        # updates csv file immediately
        update = SearchEntry()
        update.update_csv()


if __name__ == '__main__':
    instructions()
