from advanced_oop.admin import Admin
from advanced_oop.database import Database
from advanced_oop.user import User

one = Admin('Rolf', '123', 3)
two = User('Anna', '345')

for user in [one, two]:
    user.save()

print(Database.find(lambda x: x['username'] == 'Rolf'))
print(two.to_dict())

