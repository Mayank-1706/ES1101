print("Answer 1")
w = "Python is a case sensitive language"
# to find length of the string "w"
print('a)', len(w))
# to reverse the order of the string
print('b)', w[::-1])
# containing "a case sensitive" into a new string
print('c)', w[10:-9])
# replacing "a case sensitive" with "object oriented"
v = w.replace("a case sensitive", "object oriented")
print('d)', v)
# to find index of substring “a”
index = w.find('a')
print('e)', index)
# to remove the white spaces
x = w.replace(" ", "")
print('f)', x)

print("Answer 2")
# storing the required informations
Name = "Mayank Bhatnagar"
SID = "21107034"
Department = "Mechanical Engineering"
CGPA = "9.9"
print('Hey, %s Here!' % Name)
print('My SID is %s' % SID)
print('I am from %s department and my CGPA is  %s' % (Department, CGPA))

print("Answer 3")
# calculating with the help of bitwise operators
a = 56
b = 10
print('a&b=', (a & b))
print('a|b=', (a | b))
print('a^b=', (a ^ b))
print('a<<2=', a << 2, 'and', 'b<<2=', b << 2)
print('a>>2=', a >> 2, 'and', 'b>>4=', b >> 4)

print("Answer 4")
# to find whether the word “name” is present in the string entered by the user
if "name" in input("String : "):
    print("Yes")
else:
    print("No")

print("Answer 5")
# to check whether the traingle is possible or not
side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
side_3 = int(input("Enter side 3: "))

a1 = side_1 + side_2
b1 = side_2 + side_3
c1 = side_3 + side_1

x = (side_1 < b1)
y = (side_2 < c1)
z = (side_3 < a1)

answer = str(x & y & z)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print(answer)

print("Answer 6")
# to count number of bits needed to be flipped to convert ‘a’ to ‘b’
i = int(input('Enter the number a :'))
v = int(input('Enter the number b :'))

x = i^v
print(x)
