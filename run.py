#!/usr/bin/env python3.6
from user import User,
from credentials import credentials

# 1. function to create new user
def create_user(self, user_name, email, password):
    new_user = User(f user_name, email, password)
    return new_user

#  2. Function that saves User
def save_user(self):
        User.save_user()

#    3. Function that deletes user
def delete_user(self):
        User.delete_user()

        # 4. Function that finds contacts
def find_user(email):
    return  User.find_by_email(email):

  
        
