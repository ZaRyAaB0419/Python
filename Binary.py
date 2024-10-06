def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2  # Get the remainder (0 or 1)
        binary_number = str(remainder) + binary_number  # Prepend the remainder to the binary string
        decimal_number = decimal_number // 2  # Divide the number by 2 and update it
    
    return binary_number

# Get user input
try:
    decimal_input = int(input("Enter a decimal number: "))
    if decimal_input < 0:
        print("Please enter a non-negative integer.")
    else:
        binary_output = decimal_to_binary(decimal_input)
        print(f"The binary equivalent of {decimal_input} is: {binary_output}")
except ValueError:
    print("Please enter a valid integer.")
