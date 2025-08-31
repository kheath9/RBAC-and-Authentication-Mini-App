# Stores administrator and employee roles in a dictionary
users = {"admin": "administrator", "user": "employee"}


# Login simulation checks for correct username
def login(username):
    if username in users:
        return users[username]
    else:
        return None


# Separate functions for the admin and user roles
def admin_access():
    print("You have access to administrative tools.")


def user_access():
    print("You have access to employee software.")


# Input for user login
username = input("Enter your username: ")
user_role = login(username)

# Input validation
if not user_role:
    print("Invalid username. Please try again.")

else:
    print(f"Login successful! Welcome {username}. You now have {user_role} privileges.")

# Access control based on role
if user_role == "administrator":
    admin_access()  # Admin has access to admin action
elif user_role == "employee":
    user_access()  # Regular user has access to user action
