from abc import ABC, abstractmethod
from Users import Users

class UserRepository(ABC):
    
    @abstractmethod
    def save(self, user: Users):
        pass
        
    @abstractmethod
    def findById(self, userId):
        pass
    
    @abstractmethod
    def findAll(self):
        pass