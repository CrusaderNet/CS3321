# Login Entity Class
# This class is used to store the loginID and password of the user
# It has the following attributes: loginID, password and the following methods: getLoginID, setLoginID, getPassword, setPassword
# Contributors: Seth Tourish, Amin Shawa, Sanabel Elkheir, Jerami Davis
# Date: 11/26/2024
class Login:

    loginID = ""    # loginID of the user
    password = ""   # password of the user

    def __init__(self, loginID: str, password: str):    # Constructor
        self.loginID = loginID  # Initialize
        self.password = password    # Initialize

    def getLoginID(self) -> str:    # Getter for loginID
        return self.loginID   # Return loginID

    def setLoginID(self, loginID: str):  # Setter for loginID
        self.loginID = loginID  # Set loginID

    def getPassword(self) -> str:   # Getter for password
        return self.password    # Return password

    def setPassword(self, password: str):   # Setter for password
        self.password = password    # Set password