#Question9:
#Write a program to print all string starting from “N” in a list?
mylist=[]
while 1==1:
    add=input('enter some elements if the list if u are done write "done":')
    if add=='done':
        break
    mylist.append(add)
for i in mylist:
    if i.startswith('N'):
        print(i)