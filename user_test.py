import unittest
import pyperclip
from user import User
class TestUser(unittest.TestCase):

  def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user = User("Ndundiro", "ndundirokamau@gmail.com", "Kamau") #to create a user

        def test_init(self):

            self.assertEqual(self.new_user.user_name,"Ndundiro")
            self.assertEqual(self.new_user.email,"ndundirokamau@gmail.com") #Check how initialisation happens as expected.
            self.assertEqual(self.new_user.password,"Kamau")

        # Test if a new user can be saved in our list
        def test_save_user(self):
            
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

 
        check whether you can store more than one user
    
    def test_save_mutliple_users(self):
       
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

        # Test if a user can be deleted from our account

    def test_delete_user(self):
        
            self.new_user.save_user()
            test_user = User()
            test_user.save_user()
            self.new_user.delete_user()
            self.assertEqual(len(User.user_list), 1)

#find a user using username
             def test_find_user(self):
        
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        found_user = User.find_user("ndundirokamau@gmail.com")  #Uses email to verify because no two people share the same email address
        self.assertEqual(found_user.email, self.new_user.email)




        if __name__ == "__main__":
            unittest.main()

  