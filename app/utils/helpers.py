from werkzeug.security import generate_password_hash, check_password_hash

class Helpers:

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)