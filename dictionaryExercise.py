'''
users = {
    'user1':{
        'name' : 'Ali',
        'surname': 'Baba',
        'age' : 18

    },
    'user2':{
        'name' : 'Bob',
        'surname': 'Boboglu',
        'age' : 24
    },
    'user3':{
        'name' : 'Angel',
        'surname': 'Smith',
        'age' : 55

    }


}
print(users['user1']['name'])
'''

'''

students[student_number] = {
    'name' : student_name,
    'surname' : student_surname,
    'phone' : student_phone,
}
'''

#create dictionary of Students
#get inputs from users
#They will have their unique student ids which represent them
#those students will have name,surname and telefon number

print("Welcome to the System!")
students = {}
for i in range(3):
    student_number = input("Enter your id:  ")
    student_name = input("Enter your name:  ")
    student_surname = input("Enter your surname: ")
    student_phone = input("Enter your phone number: ")



    students.update({
        student_number:{
            'name' : student_name,
            'surname' : student_surname,
            'phone' : student_phone
    }
})
    print("student succesfully added")
print(students)



#Get student id and find the student

studentNo = input('student id: ')
student = students[studentNo]
print(student)













