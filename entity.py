class Login:

    loginID = ""
    password = ""

    def __init__(self, loginID: str, password: str):
        self.loginID = loginID
        self.password = password

    def getLoginID(self) -> str:
        return self.loginID

    def setLoginID(self, loginID: str):
        self.loginID = loginID

    def getPassword(self) -> str:
        return self.password

    def setPassword(self, password: str):
        self.password = password