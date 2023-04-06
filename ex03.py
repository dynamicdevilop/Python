# Q. Python Program to Find the Square Root

#Code:-

#Method - 1

userInput = int(input("Enter a Number : "))

num = pow(userInput,(1/2))

print("Square Root of "+ str(userInput) + " : " + str(num))

#Method - 2

numb = userInput ** (1/2)

print("Square Root of "+ str(userInput) + " : " + str(numb))