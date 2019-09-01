import unittest
import pyperclip
from user import User
class TestUser(unittest.TestCase):

  def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user = User("Ndundiro", "ndundirokamau@gmail.com", "Kamau") 

        def test_init(self):

            self.assertEqual(self.new_user.user_name,"Ndundiro")
            self.assertEqual(self.new_user.email,"ndundirokamau@gmail.com")
            self.assertEqual(self.new_user.password,"Kamau")

        if __name__ == "__main__":
            unittest.main()

  