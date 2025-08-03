from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

usermodel= get_user_model()

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user = usermodel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except usermodel.DoesNotExist:
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user