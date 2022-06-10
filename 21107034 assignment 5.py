#Q1
print("Q1")
string=input("Enter the string: ")
reverse_string = "" 
count = len(string)  
while count > 0:   
    reverse_string += string[ count - 1 ]
    count = count - 1 
print ("Reversed string: ",reverse_string)
print("\n")





#Q2
print("Q2")
#taking inputs for the starting and also ending of the range, also the input for the number you want to check divisibility
start=int(input("Enter the starting of the range: "))
end=int(input("Enter the ending of the range: "))
div=int(input("Enter the number you want to check the divisibility with: "))
i=start
while i<end:
    if i%div==0:
        print(i)
    i+=1
print("\n")







#Q3
print("Q3")
#taking inputs of the sides
side1=float(input("Enter the first side of the triangle: "))
side2=float(input("Enter the second side of the triangle: "))
side3=float(input("Enter the third side of the triangle: "))
x=(side1+side2+side3)/2
area=(x*(x-side1)*(x-side2)*(x-side3))**0.5
#checking the condition for the triangle to be possible or not
if side1+side2<side3:
    if side1+side3<side2:
        if side3+side2<side1:
            print("Triangle not possible")
else:
    print(area)
print("\n")





#Q4
print("Q4")
for si in range(5):
    for aj in range(si):
        print ('* ', end="")
    print('')

for si in range(5,0,-1):
    for aj in range(si):
        print('* ', end="")
    print('')
print("\n")





#Q5
print("Q5")
#taking input for rows
alpha=int(input("The number of rows to be printed: "))
o=0
for xi in range(0,alpha):
    for zi in range(xi):
            p=o//26 #we did this so that the pattern continue after Z
            #here chr(65) represents A
            print(chr(65+o-26*p), end="") 
            o+=1
    print("")
o+=1
print("\n")








#Q6
print("Q6")
#taking inputs for start and end of the range
first=int(input("Enter the starting of the range: "))
last=int(input("Enter the ending of the range: "))
#checking if number is prime or not
for px in range(first,last+1):
    for yx in range(2,px):
        if px%yx==0:
            break
    else:
        print(px)
print("\n")





#Q7
print("Q7")
a=0

while a<500:
#for divisible by 11
    if a%11==0:
#for multiple of 7
        if a%7==0:
            print(a)
    a+=1
print("\n")





#Q8
print("Q8")
number_list=[]
n=10
for i in range(1, n+1):
    print("Enter the", i ," number ")
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)
for z in number_list:
    
    if z>0:
        
        print(z,"is Positive")
    
    if z<0:
        
        print(z, "is Negative")
    
    if z%2==0:
        
        print(z, "is Even")
    
    if z%2==1:
    
        print(z,"is Odd")

count = int(input("Enter the number to be counted: "))
count = number_list.count(count)
print("It occurs ", count," times")
print("\n")







#Q9
print("Q9")
#checking occurences
ele=int(input("Enter the number of elements in the range: "))
listx=[]
for i in range(0,ele):
    t=(input("Enter in the list: "))
    listx.append(t)
occurence=(input("Enter the word to be counted: "))
occurence=listx.count(occurence)
print("It occurs", occurence, "times")
print("\n")