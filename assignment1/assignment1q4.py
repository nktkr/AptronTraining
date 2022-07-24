'''Question4:
Write a program to find the factorial of a number given by user.'''
num = int(input('enter the no: '))
fact=1
for i in range(1,num+1):
    fact=i*fact
print(fact)

