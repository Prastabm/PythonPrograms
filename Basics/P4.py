#currency converter
print("_________CURRENCY CONVERTER_________")
print("           1.INR TO USD")
print("           2.USD TO INR")
print("           3.INR TO EUR")
print("           4.EUR TO INR")
print("____________________________________")
ch=int(input("Enter your choice:"))
if(ch==1):
        print("           1.INR TO USD")
        inr=float(input("Enter currency in INR: "))
        usd=inr/82.27
        print("Value in USD: ",usd)
        
elif(ch==2):
        print("           2.USD TO INR")
        usd=float(input("Enter currency in USD: "))
        inr=usd*82.27
        print("Value in INR: ",inr)
        
elif(ch==3):
        print("           3.INR TO EUR")
        inr=float(input("Enter currency in INR: "))
        eur=inr/87.73
        print("Value in EUR: ",eur)
        
elif(ch==4):
        print("           4.EUR TO INR")
        eur=float(input("Enter currency in EUR: "))
        inr=eur*87.73
        print("Value in INR: ",inr)
        
else:
    print("wrong choice!")
        
