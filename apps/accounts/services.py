from django.contrib.auth import get_user_model

User = get_user_model()


class AccountService:
    @staticmethod
    def onboard_user(*, username: str, email: str, password: str, role: str) -> User:
        return User.objects.create_user(username=username, email=email, password=password, role=role)
