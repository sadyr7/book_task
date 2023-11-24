from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20,
                                     required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20,
                                                  required=True, write_only=True)

    class Meta:
        model = User
        fields = ('__all__')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                'Пароли должны быть похожи'
            )

        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'Пароль должен содержать буквы и цифры'
                                )

        return attrs
