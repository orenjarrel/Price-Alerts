import uuid
from src.common.utils import Utils
from src.common.database import Database
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """

        This method verifies that an e-mail/password combo (as sent by the site forms) is valid or not
        Checks that the email exists, and that the password associated to that email is correct

        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, false otherwise
        """

        user_data = Database.find_one("users", {"email": email}) # Password in sha512 -> shadf2_sha512
        if user_data is None:
            # Tell the user that their email doesn't exist
            raise UserErrors.UserNotExistsError("Your user does not exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            # tell the user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong")

        return True

    @staticmethod
    def register_user(email, password):
        """

        This method registers a user using email and password.
        The password already comes hased as sha512
        :param email: users's email
        :param password: sha512-hashed password
        :return: True if registered successfully, or False otherwise (exceptions can be raised)
        """

        user_data = Database.find_one("users", {"email": email})

        if user_data is not None:
            # Tell user they are already registered
            raise UserErrors.UserAlreadyRegisteredError("This email already exists!")
        if not Utils.email_is_valid(email):
            # Tell user that their email is not constructed properly
            raise UserErrors.InvalidEmailError("This email is not formatted correctly!")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert_method("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }

