# Q. Python Program to Solve Quadratic Equation

# Code:-


a,b,c = map(int,input("Enter the Coefficients of Quadratic Equation : ").split())
determinant = (b * b) - (4*a*c)
root1 = ((-b + (determinant**(1/2)))/2*a)
root2 = ((-b - (determinant**(1/2)))/2*a)

print("Root 1 : " + str(root1)+ " Root 2 : "+ str(root2))