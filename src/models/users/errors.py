
class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExistsError(UserError):
    # we're inheriting from UserError class
    pass


class IncorrectPasswordError(UserError):
    # we're inheriting from UserError class
    pass


class UserAlreadyRegisteredError(UserError):
    pass


class InvalidEmailError(UserError):
    pass
