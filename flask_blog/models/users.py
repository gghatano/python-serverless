from flask_login iport UserMixin

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id