from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class UserModel(AbstractUser):

    def save(self, *args, **kwargs):
        new_user = not self.pk
        super().save(* args, ** kwargs)
        if new_user:
            token = Token.objects.create(user=self)
            token.save()

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username
