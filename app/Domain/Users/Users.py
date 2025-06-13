from dataclasses import dataclass
import uuid

@dataclass
class Users:
    def __init__(
        self,
        uuid: str,
        username: str,
        email: str,
        phone: str,
        password: str = None,
    ):
        self.uuid = uuid
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    @staticmethod
    def Users(
        username: str,
        email: str,
        phone: str,
        password: str = None,
    ) -> Users:
        return Users(
            uuid=str(uuid.uuid4()),
            username=username,
            email=email,
            phone=phone,
            password=password,
        )