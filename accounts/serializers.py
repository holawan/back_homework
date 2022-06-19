from rest_framework import serializers 
from django.contrib.auth import get_user_model


User = get_user_model()
class SignupSerializer(serializers.Serializer) :

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self,validated_data) :
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user