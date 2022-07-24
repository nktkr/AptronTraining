#Question10:
#Write a program to print square of second half of elements of a list?
mylist=[]
while 1==1:
    add=input('enter some elements if the list if u are done write "done":')
    if add=='done':
        break
    mylist.append(add)
print(mylist)
fulllen=len(mylist)
halflen=fulllen//2
for i in range(halflen,fulllen):
    print(int(mylist[i])**2)

