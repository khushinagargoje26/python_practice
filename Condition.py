# Write a C program to input electricity unit charges and calculate total electricity bill according to the given condition:
#1. For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit=int(input("enter units:"))
bill=0
if(unit<=50):
    bill=unit*0.50
elif(50<unit<=150):
   bill=(unit-50)*0.75+0.50*50
elif(150<unit<=250):
    bill=(unit-150)*1.20+0.75*100+0.50*50
else:
  bill=(unit-250)*1.50+1.20*100+0.75*100+0.50*50
add_charge=bill*0.20
tot_bill=bill+add_charge
print("total electctricity bill is ",tot_bill);

# 2.	Based on annual salary tax is charged

# Less than 100000  print no tax
# Between 100000 and 150000 10% of amount excedding 1Lac
# Between 150000 and 200000  20% of amount exceeding 150000+5000
# Greater than 200000  30% of amount exceeding 200000+10000
alary=int(input("enter annual salary"))
tax=0
if(salary<=100000):
    print("no tax")
elif(100000>=salary<=150000):
    tax=(salary-100000)*0.10
elif(150000>=salary<=200000):
    tax=(salary-150000)*0.20+5000
else:
    tax=(salary-200000)*0.30+10000
print("charged tax is ",tax)

# .	Write a program to find simple intreast
# Senior citizen if the age is above 60 or else general
# SI=n*principal*roi/100
# Duration 			Roi general citizen		roi for senior citizen
# 0-2				2					2.5
# 2-4				3					3.5
# 4 -6				4					4.5
# Above 6 years		4.5					5

age = int (input("enter age "))
principal=float(input("enter principal"))
n=int(input("enter number of years"))
if(age>60):
    print("sinior citizen")
    if(0<n<=2):
        r=2.5
        
    elif(2<n<=4):
         r=3
        
    elif(4<n<=6):
         r=3.5
        
    else:
        r=4
#  5.	Library charges fine if the book is returned late
# First five days  10 rs per day
# 6 – 10 days  20 rs day
# Above 10 days  30 rs per day
day_late=int(input("number of days the book is return late"))
fine = 0
if(day_late<=5):
    fine=day_late*10
elif(day_late<=10):
    fine=(5*10)+((day_late-5)*20)
else:
    fine=(5*10)+(5*20)+((day_late-10)*30)
print("fine is",fine)

# .	Write a program to check greatest between two numbers

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if(a>b and a>c):
    print(a,"is greater")
elif(b>a and b>c):
    print(b,"is greater")
else:
    print(c,"is greater")


# Write a  program to input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
salary=float(input("enter salary:"))
if(salary<=10000):
    HRA=0.20 *salary
    DA=0.80*salary
elif(salary<=20000):
    HRA=0.25*salary
    DA=0.90*salary
else:
    HRA=0.30*salary
    DA=0.95*salary
G_salary=salary+HRA+DA 
print("gross salary is:",G_salary);



