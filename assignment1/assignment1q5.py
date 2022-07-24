'''Question5:
Write a program to print multiplication table of a given number.'''
num=int(input('hello there\nenter the no. of which u want to print the table:'))
print('the table of', num , 'goes like this')
for i in range (1,11):
    print(i*num)
