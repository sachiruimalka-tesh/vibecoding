# Grade Calculator with formatted output (name validation)

while True:
    # Validate name input
    while True:
        name = input("\nEnter student's name (or type Exit to stop): ")
        if name.lower() == "exit":
            print("Program ended.")
            exit()  # End program immediately
        elif name.isalpha():  # Check if name contains only letters
            break
        else:
            print("Invalid input! Name should contain only letters. Please try again.")

    # Input marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    # Calculate average
    average = (mark1 + mark2 + mark3) / 3

    # Determine grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Formatted output
    print("------------------------------")
    print("Name   :", name)
    print("Average:", round(average, 1))
    print("Grade  :", grade)
    print("------------------------------")
