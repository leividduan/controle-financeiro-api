class UserException(Exception):
    ...

class UserNotFoundError(UserException):
    def __init__(self):
        self.status_code = 404
        self.detail = "USER_NAO_ENCONTRADO"


class UserAlreadyExistError(UserException):
    def __init__(self):
        self.status_code = 409
        self.detail = "EMAIL_DUPLICADO"

# Category

class CategoryException(Exception):
    ...

class CategoryNotFoundError(CategoryException):
    def __init__(self):
        self.status_code = 404
        self.detail = "CATEGORIA_NAO_ENCONTRADA"


class CategoryAlreadyExistError(CategoryException):
    def __init__(self):
        self.status_code = 409
        self.detail = "NOME_DUPLICADO"