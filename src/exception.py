# Importing sys module to get exception details (like traceback, file, line number)
import sys

# Importing the custom logger from your logger file (which writes logs into .log files)
from src.logger import logging

# This function will return a detailed error message including:
# - The file name where the error occurred
# - The line number
# - The actual error message
def error_message_detail(error, error_detail: sys):
    # exc_info() gives us type, value, and traceback of the exception
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Build a detailed error message string
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    # Return the final error message
    return error_message

# Creating a custom exception class that inherits from Python's built-in Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the parent Exception class with the original error message
        super().__init__(error_message)
        
        # Generate and store the detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # When you print or log the exception, this will return the custom detailed message
    def __str__(self):
        return self.error_message


# This block runs **only** when this file is executed directly (not when it's imported)
if __name__ == "__main__":
    
    # Start logging: This line will be logged into your log file
    logging.info("Logging has started")

    # Try block to simulate an error (for demonstration)
    try:
        # This will raise a ZeroDivisionError
        a = 1 / 0
    
    # Catch any exception that occurs
    except Exception as e:
        # Log a simple message (you can improve the spelling if needed)
        logging.info("Division by zerroo")
        
        # Raise a custom exception which logs full error detail with file name and line number
        raise CustomException(e, sys)



















# import sys
# from src.logger import logging
# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in pyhon script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
#     return error_message
# class CustomException(Exception):
#     def __init__(self,error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)
#     def __str__(self):
#         return self.error_message

# # YEH NICHE WALI CHIZ BAAS DEMO KE LIYE H KI LOG FOLDER BNA AND USME HMRA YH CANT DIVIDE BY ZERO WAALA ERROR RECORD HUA
# if __name__=="__main__":
#     logging.info("Logging has started")

#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Division by zerroo")
#         raise CustomException(e,sys) 