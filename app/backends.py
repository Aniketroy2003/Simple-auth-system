from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Check if the input is an email
        if '@' in username:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None
        else:
            # If not an email, then consider username
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user
