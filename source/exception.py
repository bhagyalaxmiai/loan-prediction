import sys


def error_message_detail(error, error_detail:sys):
    # , you're accessing the exc_info method of error_detail, which returns the tuple containing
    # the exception type, exception value, and traceback object. Then you're unpacking this tuple
    # into three variables: _ (to ignore the exception type), _ (to ignore the exception value),
    # and exc_tb (to store the traceback object).
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured python script name[{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno, str(error))

    return error_message


# class LoanException extends the Exception class
class LoanException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def  __str__(self):
        return self.error_message
