# from rest_framework import status
# from rest_framework.response import Response
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer

def get_user_by_xid(customer_xid):
    try:
        user = CustomUser.objects.get(customer_xid=customer_xid)
        # serializer = CustomUserSerializer(user)
        # serialized_user = serializer.data
        # Do something with the serialized user data
        # return Response(serialized_user, status=status.HTTP_200_OK)
        return user
    except CustomUser.DoesNotExist:
        # Handle the case where the user does not exist
        # return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return None

def create_user(data):
    serializer = CustomUserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        return user
    else:
        print(serializer.errors)
        return None