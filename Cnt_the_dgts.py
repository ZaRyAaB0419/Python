def count_digits(number):
    # Convert the number to string to count the digits
    return len(str(abs(number)))  # Use abs() to handle negative numbers

# Get user input
try:
    user_input = int(input("Enter a number: "))
    digit_count = count_digits(user_input)
    print(f"The number of digits in {user_input} is: {digit_count}")
except ValueError:
    print("Please enter a valid integer.")

