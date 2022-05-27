from advanced_oop.saveable import Saveable
from advanced_oop.user import User


# class Admin inherits from User
class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

    # trial to save to DB, rewrite via Saveable class
    # def save(self):
    #     Database.insert(self.to_dict())
