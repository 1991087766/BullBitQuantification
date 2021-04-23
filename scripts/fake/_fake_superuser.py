from users.models import User


def run():
    User.objects.create_superuser(
        username="admin", password="test123456", email="navy_xu@sina.cn"
    )
    print("Superuser 'admin' was created.")
