from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer

def get_user_by_xid(customer_xid):
    try:
        user = CustomUser.objects.get(customer_xid=customer_xid)

        return user
    except CustomUser.DoesNotExist:
        # Handle the case where the user does not exist

        return None

def create_user(data):
    serializer = CustomUserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        return user
    else:
        print(serializer.errors)
        return None