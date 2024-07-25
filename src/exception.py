import sys
from logger import logging
def error_mesg_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg="Error in Python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_msg
    

class CustomExceptions(Exception):
    def __init__(self,error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_mesg_details(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg
