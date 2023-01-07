c=0
n = int(input("enter a number to check if its prime or composite number: "))
for i in range (1,n+1):
    if( n % i == 0):
        c+=1
if( c == 2 ):
    print("prime number")
else:
    print("composite number")
