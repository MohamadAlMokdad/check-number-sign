def check_number_sign():
    """
    A simple function to check whether a number is positive, negative, or zero.
    It asks the user for a number and prints the result.
    """
    # Take user input for the number
    number = input("Please enter a number: ")
    
    # Validate that the input is a valid number
    try:
        number = float(number)  # Try converting the input to a float
        if number > 0:
            print(f"{number} is a positive number.")
        elif number < 0:
            print(f"{number} is a negative number.")
        else:
            print(f"{number} is zero.")
    except ValueError:
        print("That's not a valid number! Please enter a valid number.")

# Call the function to execute it
check_number_sign()
