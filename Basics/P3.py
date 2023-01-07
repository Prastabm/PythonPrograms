#program to input a list of words and printing the longest word
n=int(input("enter the number of words you want to enter: "))
string_arr=[]
print("enter",n,"words:")
for i in range(n):
    string_arr.append(input())
maxword=string_arr[i]
for i in string_arr:
    if(len(i)>len(maxword)):
        maxword=i
print("the longest word is:",maxword)
