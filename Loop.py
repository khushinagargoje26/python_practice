#program to find palindrome number.
n= int(input("enter number"))
i=n
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse is",rev)
if(i==rev):
    print("number is palindrom")
else:
    print ("number is not palindrom")


#program to find number is armstrong or not ?
n=int(input("enter a number:"))
arm=0
temp=n
while(n!=0):
    rem=n%10
    arm=arm+rem*rem*rem
    n=n//10
if(arm==temp):
    print("number is armstrong")
else:
    print("number is not armgstrong ")

#Multiplication
n=int(input("enter the number:"))
i=1
while(i<=10):
    ans=n*i
    print(ans)
    i=i+1;
#program to find year is leap year or not 
year=int(input("enter year:"))
if(year%4==0):
    print("year is leap year",year)
elif(year%400==0):
    print("year is leap year",year)
    
else:
    print("not a leap year:",year)

#if number divided by 3 print fizz if  its divided by 5 print buzz if it is divided both print fizzbuzz
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
#print series 
n=int(input("enter a number:"))
sum=0
for i in range(2,n+1,2):
    print("1/",i,end=" ")
    sum=sum+1/i
    print("sum is ",sum)


