file = open('store/students/student_list.text', 'r')
sns = file.readline()
sns_list = sns.split(',')

if student_number not in sns_list:
    print("Student Number not Found")