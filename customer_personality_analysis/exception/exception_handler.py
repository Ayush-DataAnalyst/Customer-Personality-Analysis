class AppException(Exception):
    def __init__(self, message, error_detail):
        super().__init__(message)
        self.error_detail = error_detail
