import csv
import re


def find_by_pattern():
    csv_file = csv.DictReader(open('test.csv', "rt"), delimiter="\t")

    # find_by_pattern = input(r"Enter your pattern")
    find_by_pattern = r"(\w+)"

    names_file = open("test.csv")

    data = names_file.read()
    pattern = re.findall(find_by_pattern, data) # only the first two.

    csv_counter = 0
    pattern_counter = 0

    # print(len(pattern))

    for row in csv_file:
        csv_counter += 1
        # print("We are on ROW ", csv_counter, " of csv_file.")

        for x in set(pattern):
            pattern_counter += 1
            print("We are on ROW ", pattern_counter, " of pattern list", x)

            if x in (row['TaskTitle']):



        pattern_counter = 0  # we have to reset this number after the pattern loop ends.


if __name__ == '__main__':
    find_by_pattern()


