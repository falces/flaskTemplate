import app.Domain.Users.UserRepository as UserRepository
import app.Shared.Infrastructure.MySQLRepository as MySQLRepository

class UserMySQLRepository(MySQLRepository):
    def __init__(self):
        self.table = 'users'
        self.repository = UserRepository()
        
    def save(self, user):
        self.repository.save(user)