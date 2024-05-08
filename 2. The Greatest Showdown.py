#Task 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1>= num3:
    largestnum= num1
elif num2>= num1 and num2 >= num3:
    largestnum= num2
else:
    largestnum= num3

print("The largest number among", num1, ",", num2, ", and", num3, "is:", largestnum)

#Task 2 
if num1 <= num2 and num1<= num3:
    smallestnum= num1
elif num2<= num1 and num2 <= num3:
    smallestnum= num2
else:
    smallestnum= num3

print("The smallest number among", num1, ",", num2, ", and", num3, "is:", smallestnum)

#Task 3


