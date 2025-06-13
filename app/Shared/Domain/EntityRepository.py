class EntityRepository:
    def __init__(self, entity_class):
        self.entity_class = entity_class
        self.entities = []

    def add(self, entity):
        if isinstance(entity, self.entity_class):
            self.entities.append(entity)
        else:
            raise TypeError(f"Expected instance of {self.entity_class.__name__}")

    def getAll(self):
        return self.entities

    def findById(self, entity_id):
        for entity in self.entities:
            if entity.id == entity_id:
                return entity
        return None

    def delete(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
        else:
            raise ValueError("Entity not found in repository")