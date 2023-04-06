# Q. Python Program to Calculate the Area of a Triangle 

# Code :-


#Method - 1 


base = int(input("Enter the base of Triangle : "))
height = int(input("Enter the height of Triangle : "))
area = (base * height) / 2
print("Area of Triangle : " + str(area))


#Method - 2


a = int(input("Enter Side 1 : "))
b = int(input("Enter Side 2 : "))
c = int(input("Enter Side 3 : "))

s = (a + b + c)/2

ar = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area : " + str(ar))