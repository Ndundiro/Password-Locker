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
    #     Credentials.credentials_list = []

    def test_init(self):
        
            ## check if initialization happens as expected
        
            self.assertEqual(self.new_credential_account_name, "Facebook",)
            self.assertEqual(self.new_credential_login_detail, "0712345678")
            self.assertEqual(self.new_credential_Password, "alfiecode")

    
    #check if our credentials can be saved
    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)


        #check if users can store multiple credentials
    
        def test_saving_multiple_creds(self):
        
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)

      #  test if you can delete credentials test
        def test_delete_credentials(self): 
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

 # to test for credentials - if they are searchable.
 def test_search_for_cred(self):  
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_cred.save_cred()
        find_cred= Credentials.find_account("Instagram")
        self.assertEqual(find_cred.account, test_cred.account)
