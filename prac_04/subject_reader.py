"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def display_subject_details(subjects_data):
    pass


def main():
    """Program to load and display subject data from file."""
    subjects_data = load_subjects(FILENAME)
    display_subjects(subjects_data)

def display_subjects(subjects_data):
    for subject in subjects_data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

def subject_details(data):


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students.
    Returns a list of lists, each containing [subject_code, lecturer_name, student_count]."""
    subjects_list = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        print(data)  # See if that worked
        print("----------")
    input_file.close()


main()