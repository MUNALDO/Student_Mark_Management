Course_Infor = {}
NumOfCourse = int(input("Enter number of course : "))

def Input_Course_Infor(Infor) :
    ID = int(input("Enter course ID : "))
    name = input("Enter course name : ")
    Course = [name]
    Infor[ID] = Course

for n in range(0, NumOfCourse) :
    Input_Course_Infor(Infor=Course_Infor)
print("{:3} |{:12}".format("ID", "name"))
for key in Course_Infor :
    print("{:3} |{:12}".format(key, Course_Infor[key][0]))
