class Database:
    content = {'users': []}

    @classmethod
    def insert(cls, data):
        #cls=database
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder): #finder is a func like lambda x:x['username']!= 'Rolf'
        cls.content['users'] = [user for user in cls.content['users'] if not finder(user)]

    @classmethod
    def find(cls, finder):
        return [user for user in cls.content['users'] if finder(user)]

