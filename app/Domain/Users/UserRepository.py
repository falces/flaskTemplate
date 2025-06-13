from app.Shared.Domain.EntityRepository import EntityRepository

class UserRepository:
    def __init__(self, EntityRepository):
        self.entity_class = __class__.__name__
        self.repository = EntityRepository(self.entity_class)