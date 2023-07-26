from django import forms
from .models import UserModel

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=32)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self) -> str:
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            self.add_error("username", "This username is taken by another user")
        except UserModel.DoesNotExist:
            return username

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        try:
            UserModel.objects.get(email=email)
            self.add_error("email", "Email is already registered")
            self.add_error("email", "Email exist")
        except UserModel.DoesNotExist:
            return email

    def clean(self) -> None:
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            self.add_error("password", "Does not match")
            self.add_error("confirm_password", "Does not match")

    def save_new_user(self):
        cleaned_data = self.cleaned_data
        del cleaned_data["confirm_password"]
        return UserModel.objects.create_user(**cleaned_data)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self) -> str:
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        clean_data = self.cleaned_data
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise forms.ValidationError("Username does not exist.")

        if not user.check_password(password):
            raise forms.ValidationError("Invalid password.")

        return clean_data

