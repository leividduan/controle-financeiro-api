class UserException(Exception):
    ...

class UserNotFoundError(UserException):
    def __init__(self):
        self.status_code = 404
        self.detail = "User_NAO_ENCONTRADO"


class UserAlreadyExistError(UserException):
    def __init__(self):
        self.status_code = 409
        self.detail = "EMAIL_DUPLICADO"