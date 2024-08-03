# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6,1):
   print()
   for j in range(1,i+1,1):
       print(j,end=" ")
       j=j+1

# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

for i in range(1,6,1):
    print()
    for j in range(5,i-1,-1):
        print(j,end=" ")
        j=j+1

# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6,1):
    print()
    for i in range(1,i+1,1):
        print("*", end=" ")

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
for i in range(1,6,1):
    print()
    for j in range(1,i+1,1):
        print(i,end=" ")

# 1 
# 2 2 
# 1 2 3 
# 4 4 4 4 
# 1 2 3 4 5 

for i in range(1,6,1):
    print()
    for j in range(1,i+1,1):
        if i%2==0:
            print(i,end=" ")
        else:
            print(j,end=" ")
            j=j+1
