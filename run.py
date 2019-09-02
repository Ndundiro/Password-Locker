#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import pyperclip

# 1. function to create new user
def create_user(self, user_name, email, password):
    new_user = User(user_name, email, password)
    return new_user

#  2. Function that saves User
def save_user(self):
        User.save_user()

#    3. Function that deletes user
def delete_user(self):
	User.delete_user()

        # 4. Function that finds contacts
def find_user(email):
    return  User.find_by_email(email)

    # 5. Function that checks for existing Users
def check_existing_user(user):
    return User.check_existing_user(user)

    #6. function that saves Users
def display_users():
	return User.display_users()

	#7. Function that copies cridentials on clipboard
def copy_User_credential():
	return User.find_user(email)
# pyperclip.copy(user_found.email)

def main():
	print("Welcome to Password Safe.Please enter your name to continue:")
	name = input()
	print(f"{name}, Sign up to continue")
	print("\n")
	print("#"*50)
	print("Reply with the following short codes to navigate through Password Safe :\n sign - Sign Up,\n log - log In,\n  exit - exit ")
	print("*" *80)
	 
	code = input().lower()

	if code == "sign":
		print("Enter your details to create account")
		print("Enter Username")
		user_name = input().lower()

		print("Enter your email adress")
		email = input().lower()

		print("Enter your password")
		password = input()

		save_user(create_user(user_name, email, password))

		# Has password error...TypeError: create_user() missing 1 required positional argument: 'password

		print(f"Welcome {username} to Password Safe.You are now logged in.")

		# After Log in process

if __name__ == '__main__':
    main()  





#         else:
#             print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")
# if __name__ == '__main__':
#     main()  

        
