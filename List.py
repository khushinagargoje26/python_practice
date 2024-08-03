#1.find sum of list
l1=[22,3,44,5,677,88]
sum=0 
for i in l1:
    sum=sum+i
print(sum)

#2.find min and max number in the list
l2=[2,4,8,99,79,55]
min=l2[0]
max=l2[0]
for i in l2:
    if(i<min):
        min=i
    elif(i>max):
        max=i
print(min)
print(max) 

#3.for concate
l1=[]
n=int(input("enter numbers of  elements"))
for i in range(n):
    x=int(input("enter elements"))
    l1.append(x)
print(l1)

# 2.Take the list and append the even elements in the even list and odd elements in odd
l1=[2,44,55,77,88,66]
even_list=[]
odd_list=[]
for i in l1:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even list ",even_list)
print("odd list is",odd_list)

#3.	Take marks of 6 subjects in the list and calculate their percentage
sub=[60,40,56,77,88,90]
sum=0
for i in sub:
    sum=sum+i
total_marks=6*100
per=sum/total_marks*100
print(per)

# 4.	Input the element and check if it is present in the list or not
l1 = [1, 33, 55, 77, 99, 60]
l2 = int(input("Enter number: "))

for i in l1:
    if i == l2:
        print("Element is present")
        break
else:
    print("Element is not present")

#5 print list in ascending order and decending order
l1=[2,5,66,77,88,10,59,78]
size=len(l1)
for i in range(size):
    for j in range(size-i-1):
        if(l1[j]>l1[j+1]):
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1) 
        
for i in range(size):
    for j in range(size-i-1):
        if(l1[j]<l1[j+1]):
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1) 
  


# 6.	Write a program to print the sum of even-indexed-elements of the list minus sum of odd-indexed-elements of the list
l1=[22,47,90,55,57,23]
even_sum=0
odd_sum=0
index=0
for i in l1:
    if index%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
    index=index+i
ans=even_sum-odd_sum
print("sum of even index no minus odd index no is:",ans)

# 7.	Write a program to print the largest even number from list , if even number is not present display “no even elements”
l1=[33,57,31,43,23,90]
large_even=l1[0]
count=0
for i in l1:
    if i%2==0 and i>large_even:
        large_even=i
        
    else:
        count=count+1
if count==len(l1):
    print("there is no even number")
else:
    print("largest even number in the list is:",large_even)

# 8.to find median
l1=[33,56,66,88,23,34,11,3,2]
size=len(l1)

for i in range(size):
    for j in range(size-i-1):
        if(l1[j]>l1[j+1]):
            l1[j],l1[j+1]=l1[j+1],l1[j]
n=size
median=n//2

if n%2==1:
    median=l1[median]
    print(median)

#9.To find mean 
l1=[33,44,55,66,8,2,50]
size=len(l1)
sum=0
for i in l1:
    sum=sum+i
mean=sum/size
print("mean is",mean)

#10.To find mode
l1=[1,2,3,4,55,1,2,2]
size=len(l1)
max_count=0
for i in range(size):
    count=0
    for j in range(size):
        if l1[j]==l1[i]:
            count=count+1
    if count>max_count:
        max_count=count
        mode=l1[i]
        
print(mode)
    

        



     
