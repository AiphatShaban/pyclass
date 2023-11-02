
#import student 
#from student import Student 


from student import Student as std

std1 = std('Musa', 23, 700, 'Maths')
std2 = std('Isa', 24, 1000, 'Science') 

for s in std.students:
    print(s, '\n')