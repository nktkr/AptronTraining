#Write a program to print all the prime number from a range 0 to 100.
count=0
for i in range(2, 101):
    add=0
    for j in range (1,i//2+1):
        if i%j==0:
            add=add+1
    if add<2:
         print(i)
         count=count+1
print('no of print no form 1 to 100 is' , count)