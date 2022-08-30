dog ={"name":"Alex","color":"Black","breed": "GermanShepeard","legs": 4,"age": 5}
print(dog) #printing Dog Dictonary
student={"first_name":"Tejasai","last_name": "Kallepalli","Gender":"Male","Age":24,"marital status":"Not Married","skills":"Java","Country":"INDIA","City":"Vijayawada","Address":"Flat no :- 503 ,Firmus Pradhama Residency"}
print(student) #Printing Student Dictionary
print(len(student)) #printing length of the student dictonary
print ("Value : %s" %  student.get('skills'))
print(type(student.get('skills')))
def val_append(dict_obj, key, value):
    if key in student:
        if not isinstance(student[key], list):
            # converting key to list type
            student[key] = [student[key]]
 # Append the key's value in list
            student[key].append(value)
# calling the function to append values
val_append(student, 'skills', 'python')
print('after adding value to dictionary =\n',student)
keys_list=list(student.keys())
print(keys_list)
values_list=list(student.values())
print(values_list)