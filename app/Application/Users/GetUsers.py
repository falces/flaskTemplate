class GetUsers:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.get_all_users()