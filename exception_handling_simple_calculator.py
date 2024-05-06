#Pseudocode

# Short Message
print('='*50)
print()
print('Welcome to Simple Calculator in Python!'.center(50, ' ') + '\n')

print('='*50)

# Ask the user to choose one of the four math operations
    # 1.) Addition
    # 2.) Subtraction
    # 3.) Multiplication
    # 4.) Division

while True:
    print("\nChoose an operator from the list (1-4):")
    # Print the options with 20 spaces before each line
    print("".ljust(5) + "1. Addition (➕)")
    print("".ljust(5) + "2. Subtraction (➖)")
    print("".ljust(5) + "3. Multiplication (✖️)")
    print("".ljust(5) + "4. Division (➗)")

    # Check if the inputted option is within range or a number
    try:
        chosen_option = int(input("Enter your chosen operation: "))
        if chosen_option not in range (1, 5):
            print('‼️ Input out of range. Enter numbers 1 to 4 only. ‼️')
            continue

    except ValueError:
        print('Input invalid. Enter a valid number.')
        continue

# Ask the user for two numbers and validate input
    try:
        print()
        first_number = float(input('Enter your first number: '))
        second_number = float(input('Enter your second number: '))
    except ValueError:
        print('Input invalid. Enter a valid number.')
        continue

# Calculate the number and Display the result
    if chosen_option == 1:
        sum = (first_number) + (second_number)
        print(f">>> {first_number} + {second_number} = {sum}".center(30, ' '))
    elif chosen_option == 2:
        difference = (first_number) - (second_number)
        print(f">>> {first_number} - {second_number} = {difference}".center(30, ' '))
    elif chosen_option == 3:
        product = (first_number) * (second_number)
        print(f">>> {first_number} x {second_number} = {product}".center(30, ' '))
    elif chosen_option == 4:
        try:
            product = (first_number) / (second_number)
        except ZeroDivisionError:
            print('Cannot divide by zero.')
            continue
        else:
            print(f">>> {first_number} / {second_number} = {product}".center(30, ' '))

# Ask the user if the user wants to try again or not
    # If yes, the program will repeat
    # If no, the program will exit
    while True:
        try:
            choice = str(input("\nDo you want to continue? (y,n): "))
            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                print('\n'+'=' * 50)
                print("\nGoodbye! Thank you for using Simple Calculator.")
                exit()
            else:
                print("Invalid input!")
        except:
            print('Exiting the program\n')
            print('=' * 50)
            exit()


