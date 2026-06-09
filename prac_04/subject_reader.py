"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects_data = load_subjects(FILENAME)
    display_subjects(subjects_data)

def display_subjects(subjects_data):
    for subject in subjects_data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")



def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students.
    Returns a list of lists, each containing [subject_code, lecturer_name, student_count]."""
    subjects_list = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # Convert student count to integer and create a nested list
        subject_data = [parts[0], parts[1], int(parts[2])]
        subjects_list.append(subject_data)  # Add to our list of subjects
    input_file.close()
    return subjects_list


main()