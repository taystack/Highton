from .tools import to_datetime
from .user import User


class Group(object):
    """
        Use:
        highrise_id
        name
    """

    TYPE = 'group'

    OPTIONAL_FIELDS = [
        'name',
    ]

    def save_data(self, group):
        self.highrise_id = group['id']
        self.created_at = to_datetime(group['created-at'].pyval)
        self.updated_at = to_datetime(group['updated-at'].pyval)
        self.name = group['name']

        if hasattr(group, 'users'):
            self.set_users(group['users'])

    def set_users(self, users):
        for user in users.getchildren():
            _user = User()
            user.save_data(_user)
            self.users.append(user)
