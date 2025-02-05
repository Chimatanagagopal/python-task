# take a list which consist of numbers and find the even numbers and add even numbers to new list
list=[1,2,3,4,6]
list2=[]
list3=[]
for i in list:
    if i%2==0:
        list2.append(i)
    else:
        list3.append(i)

print('Even :',list2)
print('odd :',list3)
        

## find the sum of even and odd numbers from list 
list=[1,2,3,4,5]
b=0
c=0
for i in list:
    if i%2==0:
        b+=i
    else:
        c+=i
print('even',b)
print('odd',c)

# Make a word by taking first letter of each element list 
list=["abcd" , "efghi" , "ghifh" , "dskf" , "sdddfsdf"]
list1=""
for i in list:
    list1+=i[0]
print(list1)

# Reverse a string without taking reverse loop
str="python"
str1=''
for i in str:
    str1=i+str1
print(str1)

#1. print 1 to 100 numbers using while loop
num=1
while num<101:
    print(num)
    num+=1

# print 1 to 100 in reverse order using for Loop
print(" 1 to 100 in reverse order using for Loop")
list=[]
for i in range(1,101):
    list.append(i)
list.reverse()
print(list)

# print 1 to 100 numbers using while loop

list=[]
for i in range(1,101):
    list.append(i)
list.reverse()
print(list)

# print 1 to 100 in reverse order using while loop
n=1
rever=[]
while n<101:
    rever.append(n)
    n+=1
rever.reverse()
print(rever)

# reverse a number using while loop without string conversion
ip=1234
r=0
while ip>0:
    k=ip % 10
    r=r*10+k
    ip=ip//10
print('reverse order :',r)



    






