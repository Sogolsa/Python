first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter + to add or - to subtract: ")

if operator == "+":
    print("The sum of first_number and second_number is: " +  str(first_number + second_number))
elif operator == "-":
    print("First number - second number is: " + str(first_number - second_number))
else:
    print("Unknown operator")