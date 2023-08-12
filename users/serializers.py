from rest_framework import serializers

from users.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def validate(self, data):
        """Validate serialized data"""

        if data.get("password") != data.get("confirm_password"):
            error_message = "Password does not match"
            errors = {
                "password": error_message,
                "confirm_password": error_message
            }
            raise serializers.ValidationError(errors)

        return super().validate(data)

    def create(self, validated_data) -> UserModel:

        del validated_data["confirm_password"]

        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data) -> UserModel:
        """Update a user instance"""

        instance = super().update(instance, validated_data)

        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            instance.save()

        return instance