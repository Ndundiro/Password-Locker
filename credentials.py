class Credentials:
    
    credentials_list = []   #list of credentials to be stored here


    def __init__(self, account_name, login_detail , Password):
    
        self.account_name = account_name
        self.login_detail = login_detail
        self.Password = Password
        ''' save our accounts passwords here.'''

        

        # check if saving multiple cridentials is possible
       

        
    def save_cred(self):
            '''
            self credentials in cred_list
            '''
            Credentials.cred_list.append(self)

         
        #search for accounts
        
        @classmethod
    def find_account(cls, account):
        
        
        for cred in cls.cred_list:
            if cred.account == account:
                return cred 
