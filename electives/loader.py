from electives.model.student import Student
from electives.model.elective import Elective

def load_student_list():
    file = open('store/students/student_list.txt', 'r')
    info = file.readline()
    students = info.split(',')
    return students

def load_elective_list():
    file = open('store/electives/elective_list.txt', 'r')
    info = file.readline()
    electives = info.split(',')
    return electives

def load_student(student_number):
    file_name = 'store/students/' + str(student_number) + '.txt'
    file = open(file_name, 'r')
    info = file.readline()
    list_info = info.split(',')
    number = list_info[0]
    name = list_info[1]
    level = list_info[2]
    student = Student(student_number=number,name=name,level=level)
    elecs = file.readline(2)
    list_elecs = elecs.split(',')
    student.electives = list_elecs
    file.close()
    return student

def load_elective(crn):
    file_name = 'store/electives/' + str(crn) + '.txt'
    file = open(file_name, 'r')
    info = file.readline()
    list_info = info.split(',')
    crnn = list_info[0]
    name = list_info[1]
    year = list_info[2]
    day = list_info[3]
    time = list_info[4]
    level = list_info[5]
    instructor = list_info[6]
    description = list_info[7]
    elective = Elective(crn=crnn,name=name,year=year,day=day,time=time,level=level,
                        instructor=instructor,description=description)
    file.close()
    return elective

if __name__ == '__main__':
    pass