""" Write a program that asks for two numbers. If the sum of the numbers is greater than 100, 
print "They add up to a big number" if it is less than/equal to 100 than print "They add up to __"."""

print("Enter a number:\n")
number1 = float(input())
print("Enter a second number here: ")
number2 = float(input())

sum = number1 + number2

if sum > 100:
    print("They add up to a big number")
elif sum <= 100:
    print("They add up to ", sum)
else:
    print("error")