import synapseclient

class Auth:

    def __init__(self):
        # If you have your config file set up you can run:
        self.email= 'username'
        self.password = 'password'
        self.syn = synapseclient.login(email=self.email, password=self.password, rememberMe=True)

    def getSynObject(self):
        return self.syn

