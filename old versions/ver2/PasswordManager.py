from argon2 import PasswordHasher, exceptions

class PasswordManager:
    def __init__(self, db):
        self.ph = PasswordHasher()
        self.db = db
        self.hashed_password = self.db.get_password() or ""  # load from DB

    def set_password(self, plain_password: str):
        if plain_password == "":
            self.hashed_password = ""
        else:
            self.hashed_password = self.ph.hash(plain_password)
        self.db.set_password(self.hashed_password)

    def verify_password(self, plain_password: str) -> bool:
        if not self.hashed_password:
            return plain_password == ""
        try:
            return self.ph.verify(self.hashed_password, plain_password)
        except exceptions.VerifyMismatchError:
            return False
