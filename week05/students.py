import csv

STUDENT_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    student_list = read_dictionary("students.csv", STUDENT_NUMBER_INDEX)
    student_i_number = input("Please enter your I-number: ")
    student_i_number = student_i_number.replace("-", "")
    
    if len(student_i_number) < 9:
        print("Invalid I-number: too few digits")
    elif len(student_i_number) > 9:
        print("Invalid I-Number: too many digits")
    elif student_i_number.isdigit():
        print("Invalid student number")
    else:
        if student_i_number not in student_list:
            print("No such student")
        else:
            print(student_name[NAME_INDEX])

    if student_i_number not in student_list:
        print("No such student.")
    else:
        student_name = student_list


def read_dictionary(filename, stud_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            stud_id = row[stud_index]
            dictionary[stud_id] = row

    return dictionary

if __name__ == "__main__":
    main()