#Q1
x=float(input("Enter Marks Obtained: "))
#taking input of the marks 
if x<=25:
        print("GRADE: F")
if 25<=x<45:
        print("GRADE: E")
if 45<=x<50:
        print("GRADE: D")
if 50<=x<60:
        print("GRADE: C")
if 60<=x<80:
        print("GRADE: B")
if x>=80:
        print("GRADE: A")
if x>100:
        print("Invalid Input")
#grading the marks accordingly



#Q2
r = int(input("Enter the year: "))
#taking input of the required year
if r%4 == 0:
    if r%100 == 0:
        if r%400 == 0: #satisfying the required conditions
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")



#Q3
from random import randint
for y in range(1,11):
    a = randint(1,10)
    b = randint(1,10)
#rand function is used to select a random integer
    print("Q" + str(y) + " is: " + str(a) +"x"+ str(b) + " = ")
    ans = int(input())
    #provide the answer
    if ans == a*b:
        print("Right!")
    else:
        print("Wrong!")
        



#Q4
#taking the range 
for l in range(200):
    if l%5 != 2:
        if l%6 != 3:
            if l%7 != 2:
                print("There are " + str(l) + " candies in total")