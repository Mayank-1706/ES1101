#Q1
print("SOLUTION 1")
print("\n")
a=int(input("Enter the number: "))
l=[]
i=1
while i<a:
    if a%i==0:
        l.append(i)
    i+=1
print(l)
if sum(l)==a:
    print("The number is perfect")
else:
    print("The number is not perfect")

print("\n")




#Q2
print("SOLUTION 2")
print("\n")
phrase=input("Enter the word,phrase or sequence: ")
phrase = phrase.lower()
def checkPalindrome():
    string2 = phrase.replace(" " , "")
    rev_string = string2[::-1]
    if rev_string == string2:
        print(f"{phrase} is a palindrome.")
    else:
        print(f"{phrase} is not a palindrome")

checkPalindrome()

print("\n")



#Q3
print("SOLUTION 3")
print("\n")
from math import factorial

n=int(input("Enter the number of rows for Pascal triangle: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range (i+1):
        print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
    print()




print("\n")




#Q4
print("SOLUTION 4")
print("\n")
string = input("Enter the string to check for a pangram: ")
string.lower()
def checkPangram():
    for i in range(1,27):
        c = chr(64+i)
        c = c.lower()
        
        index = string.find(c)
        if index == -1:
            print("It is not a pangram.")
            a = 0
            break
        else:
            a = 1
            
    if a == 1:
        print("It is a pangram")


checkPangram()




print("\n")



#Q5
print("SOLUTION 5")
print("\n")

input_string=str(input("enter a hyphen separated sentence: "))

li=list(input_string.split("-"))
li.sort()

print("-".join(li))






print("\n")




#Q6
print("SOLUTION 6")
print("\n")



def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Maynank","Mechanical",21107034)








print("\n")



#Q7
print("SOLUTION 7")
print("\n")

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()





print("\n")











#Q8
print("SOLUTION 8")
print("\n")








print("\n")





#Q9
print("SOLUTION 9")
print("\n")

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")






print("\n")