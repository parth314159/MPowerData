import synapseclient

class Auth:

    def __init__(self):
        # If you have your config file set up you can run:
        self.email= 'shahparth8891@gmail.com'
        self.password = 'P@rth8891'
        self.syn = synapseclient.login(email=self.email, password=self.password, rememberMe=True)

    def getSynObject(self):
        return self.syn

