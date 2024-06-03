import bcrypt

# Dictionary to store user information
users = {}


# Function to handle user registration
def register_user():
    username = input("Enter username: ")
    if username in users:
        print("Username already taken. Please try again.")
        return

    password = input("Enter password: ")
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_password
    print("User registered successfully!")


# Function to handle user login
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("Username not found. Please register first.")
        return False

    hashed_password = users[username]
    if bcrypt.checkpw(password.encode(), hashed_password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password. Please try again.")
        return False


# Function to access the secured page
def secured_page():
    print("Welcome to the secured page!")


# Main function to run the authentication system
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                secured_page()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
