class MySQLRepository:
    def __init__(self):
        pass
    
    def getAll(self, model):
        return model.query.all()
    
    def save(self, model):
        pass