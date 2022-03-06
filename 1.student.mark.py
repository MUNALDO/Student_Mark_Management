Course_Infor = {}
student_info = {}
NumOfCourse = int(input("Enter number of course : "))
num_student = int(input("Input number of students: "))


def Input_Course_Infor(Infor):
    ID = int(input("Enter course ID : "))
    name = input("Enter course name : ")
    Course = [name]
    Infor[ID] = Course


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


for n in range(0, NumOfCourse):
    Input_Course_Infor(Infor=Course_Infor)
    
print("{:3} |{:12}".format("ID", "name"))
for key in Course_Infor:
    print("{:3} |{:12}".format(key, Course_Infor[key][0]))

for i in range(0, num_student):
    input_student_info(info=student_info)
    list_student()
