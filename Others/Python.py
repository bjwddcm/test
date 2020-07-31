student = {'小梦':'1001','小智':1002,'小强':1003}
student['小强'] = '1005'

print('小强的学号是:%(小强)s' % student)

del student['小梦']
print(student)

a = len(student)
print("length: %d"   %  len(student))

print(type(student))

teacher = student.copy('小智')

print(teacher)