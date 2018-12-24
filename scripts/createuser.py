from app.operations import User
import getpass

class ManualActions:
    def create_user():
        username = input("Username: ")
        password = getpass.getpass()
        email = input("Email: ")
        role = input("Role: ")
        print(User().create(username, password, email, role))


if __name__ == "__main__":
    ManualActions.create_user()
