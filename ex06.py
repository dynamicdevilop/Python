# Q. Python Program to Swap Two Variables

# Code :-


a,b = map(int,input("Enter Two Numbers : ").split())

print("Before Swapping")
print("a = " + str(a) + " b = "+ str(b))

a = a - b
b = a + b
a = b - a 

print("After Swapping")
print("a = " + str(a) + " b = "+ str(b))