from tuitions import Payment
from student import Student

print('Setting Fees:')

tuition = int(input('Enter Tuition: '))
lib_fee = int(input('Enter Lib Fee: '))
func_fee = int(input('Enter function fees: '))
med_fee = int(input('Enter Medical fee: '))
#set_total_fees(cls, tuition, lib_fee, func_fee, med_fee):
if type(tuition) is int:
    Payment.set_total_fees(tuition, lib_fee, func_fee, med_fee)
    print(f'Total fees is {Payment.get_total_fees()}')
else:
    print('Wrong datatype entered')

i=0
choice = True
while(choice):
    print(f"Enter Student {i+1} details")
    name = input('Enter Students name: ')
    age = input('Enter Students age: ')
    fees = int(input('Enter Fees paid by the Students: '))
    std1 = Student(name, age, fees)
    opt = input('Would you like to enter more students (Yes/No)')
    i+=1
    if opt.upper() == 'NO':
        choice = False 

stds = std1.get_all_students()

# print('These are all the Students')
i=0
for std in stds:
    print(f'Student {i+1}')
    print(std,'\n')
    i+=1

print('These are students that have paid')
paid_stds = Payment.get_paid_std()

i=0
for pa in paid_stds:
    print(f'Student {i+1}')
    print(pa)
    i+=1
