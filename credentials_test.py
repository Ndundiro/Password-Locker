import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    # The setUp() method allows us to define instructions that will be executed before each test method
    def setUp(self):    
        self.new_credentials = Credentials("Facebook", "0712345678", "alfiecode")
    

    The tearDown() method allows us to clean up.
    # def tearDown(self):
    #     Credentials.credentials_list = []

    def test_init(self):
        
            ## check if initialization happens as expected ............1
        
            self.assertEqual(self.new_credential_account_name, "Facebook",)
            self.assertEqual(self.new_credential_login_detail, "0712345678")
            self.assertEqual(self.new_credential_Password, "alfiecode")

    
    #check if our credentials can be saved............2
    def test_save_credentials(self):

        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.credentials_list),1)


        #check if users can store multiple credentials..................3
        def test_saving_multiple_creds(self):
        
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)

      #  test if you can delete credentials test ...............4
        def test_delete_credentials(self): 
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

      # to test if credentials are searchable..................5
        def test_search_for_cred(self):  
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_cred.save_cred()
        find_cred= Credentials.find_account("Instagram")
        self.assertEqual(find_cred.account, test_cred.account)

        # test if all credentials can be displayed.....................6
     def test_display_credentials(self): 
        
        self.assertEqual(Credentials.display_cred(), Credentials.cred_list)


        # not confirmed if actuallly they exist
        # copy credential on clip board
