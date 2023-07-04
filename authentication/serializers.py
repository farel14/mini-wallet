from rest_framework import serializers
from authentication.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['customer_xid']

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.save()

        return user
