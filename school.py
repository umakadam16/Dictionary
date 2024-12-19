# Each student in a school is associated with their grade.
student_name={'ram':'A',
              'sita':'B',
              'sitara':'C',
              'rina':'B'}
print(student_name)
# Addng new student name in dictionary
student_name['tanvi']='c'
student_name['Amar']='A+'
print("Adding new stuent name :",student_name)
#deleting studen name in dictionarary
del student_name['rina']
print("dictionary after deleting student name",student_name)
# updating dictionary
student_name['sita']='A+'
print("after updating dictionary:",student_name)
#is avilablae in dictionary
is_rina_in_list = 'rina' in student_name
print("avilable student is:",is_rina_in_list)




