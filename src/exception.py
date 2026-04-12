import sys
import logging
#sys module is used to get the details of the error like which line the error is coming from and which file the error is coming from
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()#first two are not imp but third exc_tb gives info about exception
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]"
    file_name,exc_tb.tb_lineno,str(error)
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)
    def __str__(self):
        return self.error_message
