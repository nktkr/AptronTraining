#Question2:
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
#digit of the number is an even number.

for i in range (1000,3000):
    k=str(i)
    k0=int(k[0])%2
    k1=int(k[1])%2
    k2=int(k[2])%2
    k3=int(k[3])%2
    sum=k0+k1+k2+k3
    if sum==0:
        print(i)
