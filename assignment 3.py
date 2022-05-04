# Q1
import math
print("Answer 1")
a = int(input('Enter the number :'))
x = bin(a)
print(x)

# Q2
print("Answer 2")
term_math = input('Enter a mathematical expression:')
print('Result :', eval(term_math))

# Q3
import math
print("Answer 3")
# a
print("a)", (3 + 4) * 5)
# b
n =int(input("Enter the valuse of n :",))
print("b)", n*(n - 1) / 2)
# c
r1 = float(input('Radius :'))
print("c)", 4 * math.pi * r1 ** 2)
# d
r = float(input('Radius :'))
a = int(input('Value of angle A in radians :'))
b = int(input('Value of angle B in radians :'))
print("d)", ((r * ((math.cos(a)) ** 2)) + (r * ((math.sin(b)) ** 2))) ** 0.5)
# e
x1 = int(input("Value for x1 :"))
y1 = int(input("Value for y1 :"))
y2 = int(input("Value for y2 :"))
x2 = int(input("Value for x2 :"))
eq = (y2 - y1) / (x2 - x1)
print("e)", eq)

# Q4
print("Answer 4")
print("In the range(5) ,sequence of numbers that would be generated")
for i in range(5):
    print(i)

print("In the range(3, 10) ,sequence of numbers that would be generated")
for i in range(3, 10):
    print(i)

print("In the range(4 ,13, 3) ,sequence of numbers that would be generated")
for i in range(4, 13, 3):
    print(i)

print("In the range(15, 5, -2) ,sequence of numbers that would be generated")
for i in range(15, 5, -2):
    print(i)

print("In the range(5, 3) ,sequence of numbers that would be generated")
for i in range(5, 3):
    print(i)

# Q5
print("Answer 5")
C = int(input('Enter the number of Carbon Atoms :'))
H = int(input('Enter the numbwer of Hydrogen Atoms :'))
O = int(input('Enter the number of Oxygen Atoms :'))

Molecular_weight = C * 12.0107 + H * 1.00794 + O * 15.9994
print('The Molecuar weight of given compound is: ', Molecular_weight)
