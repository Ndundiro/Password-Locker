class Credentials:
    
    credentials_list = []   #list of credentials to be stored here


    def __init__(self, account_name, login_detail , Password):
    
        self.account_name = account_name
        self.login_detail = login_detail
        self.Password = Password
        ''' save our accounts passwords here.'''

        

        # check if saving multiple cridentials is possible .....................1
    def save_credentials(self):
        Credentials.credentials_list.append(self)


       # delete created credentials off our list
    def delete_credentials(self):        
        Credentials.credentials_list.remove(self) 

         
        #search for accounts
    @classmethod
    def find_account(cls, account):
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials 

    
