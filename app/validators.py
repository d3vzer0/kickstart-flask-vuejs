import hashlib
import mongoengine
from app.models import Users


class Validate:
    def login(username, password):
        try:
            userobject = Users.objects.get(username=username)
            salt = userobject.salt
            passhash = hashlib.sha512()
            passwordhash = salt + password
            passhash.update(passwordhash.encode('utf-8'))
            passhash = str(passhash.hexdigest())

            if passhash == userobject.password:
                result = {'result': 'success', 'message': 'Succesfull login',
                          'data': userobject}

            else:
                result = {'result': 'failed',
                          'message': 'Wrong username and/or password'}

        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed",
                      "message": "Wrong username and/or password"}

        return result

    def identity(payload):
        try:
            user_id = payload['identity']
            username = Users.objects.get(id=user_id)['username']
            return username

        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed",
                        "message": "Invalid identity"}


    def admin(user_id):
        try:
            userobject = Users.objects.get(id=user_id, role="administrator")
            result = {"result": "success", "message": "User role is admin"}

        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed", "message": "User does not exist"}

        return result
