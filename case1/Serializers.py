from rest_framework import serializers

from case1.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'user_last_name', 'dob')

