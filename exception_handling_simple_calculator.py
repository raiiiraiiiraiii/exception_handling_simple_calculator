#Pseudocode

# Short Message
print('='*50)
print('\nWelcome to Simple Calculator in Python!')

# Ask the user to choose one of the four math operations
    # 1.) Addition
    # 2.) Subtraction
    # 3.) Multiplication
    # 4.) Division

while True:
    print("\nChoose an operator from the list (1-4): \n"
          " 1. Addition (➕)\n"
          " 2. Subtraction (➖)\n"
          " 3. Multiplication (✖️)\n"
          " 4. Division (➗)\n"
          " 5. Exit\n")

# Check if the inputted option is within range or a number
    try:
        chosen_option = int(input("Enter your chosen operation: "))
        if chosen_option not in range (1, 4+1):
            print('‼️ Input out of range. Enter numbers 1 to 5 only. ‼️')
            continue
        if chosen_option == 5:
            break

    except ValueError:
        print('Input invalid. Enter a valid number.')
        continue

# Ask the user for two numbers and validate input
    try:
        first_number = float(input('Enter your first number: '))
        second_number = float(input('Enter your second number: '))
    except ValueError:
        print('Input invalid. Enter a valid number.')
        continue

# Display the result

# Ask the user if the user wants to try again or not
    # If yes, the program will repeat
    # If no, the program will exit