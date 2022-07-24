#Question8:
#Find sum of all elements in the given list l=[18,82,[57,94,73],33,29,58]
list1=[18,82,[57,94,73],33,29,58]
add=0
for i in range(len(list1)):
    if i==2:
        for j in list1[2]:
            add=add+j
    else:
        add=add+list1[i]
print(add)