from app.Domain.Users.Exceptions import UserNotFound
from app.Domain.Users.UserRepository import UserRepository
from app.Domain.Users.Users import Users

class UsersService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
    def createUser(self, data) -> Users:        
        user = Users.Users(
            username=data.get('username'),
            email=data.get('email'),
            phone=data.get('phone'),
            password=data.get('password')
        )
        
        self.repository.save(user)
        return user
    

    def getUsers(self):
        return self.repository.findAll()
    
    def getUser(self, userId):
        user = self.repository.findById(userId)
        if not user:
            raise UserNotFound(f"User with id {userId} not found")
        return user