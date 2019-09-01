import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_credentials = Credentials("Facebook", "0712345678", "alfiecode")
    
    # def tearDown(self):
    #     '''
    #     clear list before any test is run
    #     '''
    #     Credentials.cred_list = []