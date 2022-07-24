'''Question7:
Use a loop to display elements from a given list present at odd index positions '''
mylist=[]
while 1==1:
    add=input('enter the elements if the list if u are done write "done":')
    if add=='done':
        break
    mylist.append(add)
print('the list entered by you is ' , mylist)

for i in range(len(mylist)):
    if i%2!=0:
        print(mylist[i])
