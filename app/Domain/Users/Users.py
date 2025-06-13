from dataclasses import dataclass
import uuid

@dataclass
class Users:

    def getUser(self, id):
        return {
            id: name,
            "ID": id,
        }
    
    @staticmethod
    def Users(
        username: str,
        email: str,
        phone: str,
    ) -> Users:
        return Users(
            uuid=str(uuid.uuid4()),
            username=username,
            email=email,
            phone=phone,
        )