from django.contrib.auth.backends import BaseBackend
from .models import MyUser

class MyUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None