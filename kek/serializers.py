from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='username', validators=[UniqueValidator(queryset=User.objects.all())])
    pwd = serializers.CharField(source='password')

    class Meta:
        model = User
        fields = ['user', 'pwd', 'email']

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавьте дополнительные поля в JWT-токен (опционально)
        token['email'] = user.email

        return token


