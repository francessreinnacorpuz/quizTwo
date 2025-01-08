# Function to register a user and store their details in a dictionary
def register_user():
    user_details = {}
    user_details["first_name"] = input("Enter your first name: ")
    user_details["last_name"] = input("Enter your last name: ")
    user_details["course"] = input("Enter your course: ")
    user_details["year_level"] = input("Enter your year level: ")
    user_details["section"] = input("Enter your section: ")
    user_details["username"] = input("Enter your username: ")
    user_details["password"] = input("Enter your password: ")
    user_details["pin_code"] = input("Enter your pin code (max 8 digits): ")

    while len(user_details["pin_code"]) > 8:
        print("Pin code should not exceed 8 digits. Please try again.")
        user_details["pin_code"] = input("Enter your pin code (max 8 digits): ")

    print("Congratulations! You have successfully registered.")
    return user_details

# Function to log in a user
def login_user(user_details):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == user_details["username"] and password == user_details["password"]:
            while True:
                pin_code = input("Enter your pin code: ")
                if pin_code == user_details["pin_code"]:
                    print("Login successful!")
                    print("Your registered information:")
                    print(f"Name: {user_details['first_name']} {user_details['last_name']}")
                    print(f"Course: {user_details['course']}")
                    print(f"Year Level: {user_details['year_level']}")
                    print(f"Section: {user_details['section']}")
                    break
                else:
                    print("Incorrect pin code. Please try again.")
            break
        else:
            print("Incorrect username or password. Please try again.")

# Function to store lengths of student and classmate names in a list
def store_name_lengths(student_name, classmate_name):
    name_lengths = [len(student_name), len(classmate_name)]
    return name_lengths

# Function to reverse sort a list of class numbers
def reverse_sort_class_numbers(class_numbers):
    class_numbers.sort(reverse=True)
    return class_numbers

# Callable function with IF...ELIF...ELSE conditions
def quiz_two(user_name):
    if len(user_name) < 5:
        print(f"{user_name}, your name is short!")
    elif len(user_name) >= 5 and len(user_name) <= 10:
        print(f"{user_name}, your name is of medium length!")
    else:
        print(f"{user_name}, your name is long!")

# Main function to control the program flow
def main():
    # Register a user
    user_details = register_user()

    # Ask if the user wants to log in
    while True:
        choice = input("Do you want to log in? (yes/no): ")
        if choice.lower() == "yes":
            login_user(user_details)
            break
        elif choice.lower() == "no":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

    # Store student and classmate names and their lengths
    student_name = input("Enter the student's name: ")
    classmate_name = input("Enter the classmate's name: ")
    name_lengths = store_name_lengths(student_name, classmate_name)
    print(f"Lengths of names: {name_lengths}")

    # Reverse sort a list of class numbers
    class_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_class_numbers = reverse_sort_class_numbers(class_numbers)
    print(f"Reverse sorted class numbers: {sorted_class_numbers}")

    # Ask for user input and call quiz_two()
    user_name = input("Enter your name: ")
    quiz_two(user_name)

# Call the main function to run the program
if __name__ == "__main__":
    main()