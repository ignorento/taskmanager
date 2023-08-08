from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username
