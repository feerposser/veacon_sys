from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from user_veacon.models import UserVeaconModel


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserVeaconSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserVeaconModel
        fields = ('user', 'phone')
