student_info = {
    "name": "shradha",     
    "cgpa": [9.6],
    "marks": [98, 97, 95]
}
print(student_info)


# question number 2
# Initialize variables for sum and count
even_sum = 0
count = 0
i = 1

# While loop to iterate from 1 to n
while i <= n:
    if i % 2 == 0:
        even_sum += i  # Add the even number to the sum
        count += 1  # Increment the count of even numbers
    i += 1  # Move to the next number

# Print the results
print("Sum of even numbers up to", n, "is:", even_sum)
print("Total count of even numbers up to", n, "is:", count) 

# the second question is q 3

# Prompt the user to enter a positive integer
n = int(input("Enter a positive integer to calculate its factorial: "))

# Validate the input: repeat asking until a positive integer is entered
while n <= 0:
    print("The number must be a positive integer.")
    n = int(input("Please enter a positive integer: "))

# Initialize variables for factorial calculation
factorial = 1
i = 1

# While loop to calculate the factorial
while i <= n:
    factorial *= i  # Multiply the current value of factorial by i
    i += 1  # Move to the next number

# Print the result
print("The factorial of", n, "is:", factorial)
