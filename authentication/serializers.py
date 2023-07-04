# from rest_framework import serializers
# # from django.contrib.auth.models import User
# from .models import CustomUser
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password


# class RegisterSerializer(serializers.ModelSerializer):
#     # email = serializers.EmailField(
#     #     required=True,
#     #     validators=[UniqueValidator(queryset=User.objects.all())]
#     # )

#     # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     # password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ('id','customer_xid')

#     # def validate(self, attrs):
#     #     if attrs['password'] != attrs['password2']:
#     #         raise serializers.ValidationError({"password": "Password fields didn't match."})

#     #     return attrs

#     def create(self, validated_data):
#         # del validated_data['password2']
#         user = CustomUser.objects.create(**validated_data)

#         # user.set_password(validated_data['password'])
#         user.save()

#         return user


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

class CustomUserInitSerilizer(serializers.ModelSerializer):
    # token = serializers.UUIDField()
    token = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ['token']
