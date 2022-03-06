course_info = {}
student_info = {}
course_with_mark = {}
end = False

def Input_Course_Infor(Infor):
    id = int(input("Enter course ID : "))
    name = input("Enter course name : ")
    course = [name]
    Infor[id] = course


def input_student_info(info):
    id = input("Input student's ID: ")
    name = input("Input student's name: ")
    dob = input("Input student's date of birth (dd/mm/yyyy): ")
    student = [name, dob]
    info[id] = student


def list_student():
    print("{:10} | {:20} | {:20}".format("ID", "Name", "Date of Birth"))
    for key in student_info:
        print("{:10} | {:20} | {:20}".format(key, student_info[key][0], student_info[key][1]))


def list_course():
    print("{:3} | {:12}".format("ID", "name"))
    for key in course_info:
        print("{:3} | {:12}".format(key, course_info[key][0]))


def add_mark_to_course():
    course_with_mark = course_info


def is_empty(dict):
    if len(dict) == 0:
        return True
    return False


print("Welcome To Student Management Program!")
while not end:
    print("-----------menu----------")
    print("[1] Add Students")
    print("[2] Add Courses")
    print("[3] Show list of students")
    print("[4] Show list of courses")
    print("[5] Add student's marks to a course")
    print("[6] Show a course with marks")
    print("[0] Exit")
    choice = int(input("Please choose an option: "))
    if choice == 1:
        num_student = int(input("Input number of students: "))
        for i in range(0, num_student):
            input_student_info(info=student_info)
    elif choice == 2:
        NumOfCourse = int(input("Enter number of course : "))
        for n in range(0, NumOfCourse):
            Input_Course_Infor(Infor=course_info)
    elif choice == 3:
        empty = is_empty(student_info)
        if not empty:
            list_student()
        else:
            print("There are no students in class!")
    elif choice == 4:
        empty = is_empty(course_info)
        if not empty:
            list_course()
        else:
            print("There are no courses!")
    elif choice == 5:
    elif choice == 6:
    elif choice == 0:
        end = True
    else:
        print(f"{choice} is an invalid input!")
