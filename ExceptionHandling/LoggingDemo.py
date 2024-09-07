import logging

logging.basicConfig(filename="mylog.log", level=logging.ERROR)
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.debug("Debug")
logging.info("Info")