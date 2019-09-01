import pyperclip
class User:


    '''
    Class that generates new instances of user
    '''
    user_list = []  # list of users to be stored here

    def __init__(self, user_name, email, password):
        '''
        saving user credentials into user_list for login
        '''
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_user(self):
        User.user_list.append(self)
