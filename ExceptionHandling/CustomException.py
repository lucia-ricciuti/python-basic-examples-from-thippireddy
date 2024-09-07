import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

class OverTheLimitException(Exception):
    def __init__(self, message):
        self.message = message

def withdraw(amount):
    if (amount > 500):
        logging.error("Over the limit Exception")
        raise OverTheLimitException("You cannot withdraw more than 500 dollars per day")

withdraw(600)
