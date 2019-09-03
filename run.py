#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import pyperclip

# 1. function to create new user
def create_user(self, user_name, email, password):
	'''
	function to create new user
	'''
	new_user = User(user_name, email, password)
	return new_user

#  2. Function that saves User
def save_user(self):
	'''
	Function that saves User
	'''
	User.save_user()


#    3. Function that deletes user
def delete_user(self):
	'''
	Function that deletes user
	'''
	User.delete_user()

        # 4. Function that finds user when one choses to log in.
def find_user(email, password):
	'''
	Function that finds user when one choses to log in.
	'''
	return  User.find_user(email, password)

    # 5. Function that checks for existing Users
# def check_existing_user(user):
'''
Function that checks for existing Users
'''
#     return User.check_existing_user(user)

    #6. function that saves Users
def display_users():
	'''
	function that saves Users
	'''
	return User.display_users()

	#7. Function that copies cridentials on clipboard
def copy_User_credential():
	'''
	Function that copies cridentials on clipboard
	'''
	return User.find_user(email)
# pyperclip.copy(user_found.email)

def main():
	print("Welcome to Password Safe.Follow through our Menu and enter the shortcode to navigate:\n sign ---- to sign up,\n log ----   to log In,\n  exit ---- to exit ")
	
	# print("Reply with the following short codes to navigate through Password Safe :\n sign - Sign Up,\n log - log In,\n  exit - exit ")
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

		save_user( user_name, password)

		# Has password error...TypeError: create_user() missing 1 required positional argument: 'password

		print(f"Welcome {user_name} to Password Safe.You are now logged in.")

		# Accessible to Users who have already logged in Only
		print("Use the following shortcodes to proceed : create - create new account details,\n display - display accounts,\n find - find an account,\n generate - generate random password,\n exit - exit the Application")
		
		if code == "create":
			print("Please enter the Account details for the password you want to save: ")
			print("Account name")
			account = input()
			print("LogIn cridential used.eg. phone number,email ")
			email = input()
			print ("Enter the password used")
			password = input()
			save_cred(create_credentials(user_name, email, password))
			print("Your account credentials have been saved.Enter  display to view or enter create to add another account.")

			save_user(create_user(user_name, email, password)) # create and save new passlock.
			save_credentials(create_credentials(user_name, email, password))

			print ("\n")
			print(f"A new user,with a user name {user_name} and email {email} has been added")
			
			print("Dear User,please use the given shortcodes to proceed")



	elif code == "log":  #create the log in logic if user already has an account
		
		print("Enter your  Username")
		user_name = input().lower()

		# print("Enter your email adress")
		# email = input().lower()

		print ("Enter your password")
		password = input()

		if find_user(user_name, password) == password:  #can take user_name as the third parameter
			print("Successfully logged in")	

		else:
			print("Your cridentials don't match any account.Enter the shortcode sign, to Sign up and access Application.")






	elif code =="exit":
		print("Logging Out ... .  .   .    .     .      .         .       .")

		print("\n")	
		print("Adios,Have a nice time!")




	else:
		print("Dear User,you have entered an invalid shortcode.Please enter the following short codes to access Password Safe:\n sign - Sign Up,\n log - log In,\n  exit - exit ")

if __name__ == '__main__':
    main()  

        
