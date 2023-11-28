#calling the class method of dictionary
'''
students_attendance = dict()
print(type(students_attendance),type(2))


def insert_data(roll_no, classes_attended):
    students_attendance[roll_no]= classes_attended

insert_data("B Bharath", 100)
insert_data("K Bharath",40)
insert_data("Surya",70)

print(students_attendance)

def fetch_data(roll_no):
    return students_attendance.get(roll_no,-5)

print(students_attendance)

def update_data(roll_no, updated_attendance):
    students_attendance[roll_no]= updated_attendance

update_data("B Bharath",94)
update_data("K Bharath",60)
print(students_attendance)

def remove_data(roll_no):
    del students_attendance[roll_no]

remove_data("Surya")
print(students_attendance)
'''

attendance_dict = [None]*10
def hashFunction(name):
    total=0
    for i in name:
        print(f"{i} ---> {ord(i)}")
        total+=ord(i)
    print(total)
    index = total%10
    return index
hashFunction("selvam")

def setter(key,value):
    index = hashFunction(key)
    attendance_dict[index] = value

def getter(key,value):
    index = hashFunction(key)
    return attendance_dict[index]

setter('Shashank',10)
setter("Rajit",40)
setter("Vel",50)

