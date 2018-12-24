from app import db
import mongoengine

# Filter options can be defined like so
filter_options = ('administrator', 'user')


# An example class of a user MongoDB document, containing
class Users(db.Document):
    # Define a key field by specifying unique=True
    # Combination of fields as a key is available with
    # unique_with=['field1', 'field2']
    username = db.StringField(max_length=50, required=True, unique=True)
    password = db.StringField(max_length=128, required=True)
    email = db.EmailField(required=True)
    salt = db.StringField(required=True, max_length=128)
    role = db.StringField(required=True, choices=filter_options)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
