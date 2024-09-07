class InvalidPasswordException(Exception):
    
    def __init__(self, message):
        self.message = message
        
    
psw = input("Enter your password: ")
try:
    if len(psw) < 8:
        raise InvalidPasswordException(f"Password is only {len(psw)} characters long. It should be at least 8.")
except InvalidPasswordException as obj:
    print("Password is not valid.", obj)
else:
    print("Password is valid.")
