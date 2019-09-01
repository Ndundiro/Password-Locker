class Credentials:
    
    credentials_list = []   #list of credentials to be stored here


    def __init__(self, account_name, login_detail , Password):
    
        self.account_name = account_name
        self.login_detail = login_detail
        self.Password = Password
        ''' save our accounts passwords here.'''

        def test_init(self):
        
            ## check if initialization happens as expected
        
            self.assertEqual(self.new_credential_account_name, "Facebook",)
            self.assertEqual(self.new_credential_login_detail, "0712345678")
            self.assertEqual(self.new_credential_Password, "alfiecode")

        # check if saving multiple cridentials is possible
        def test_save_credentials(self):
  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)
