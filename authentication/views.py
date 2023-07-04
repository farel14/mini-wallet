from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from .models import CustomUser
from mini_wallet import response_util


@api_view(['POST'])
def init_user_view(request):
    customer_xid = request.data.get('customer_xid')

    if not customer_xid:
        return response_util.response_wrapper({"customer_xid": ["Missing data for required field."]}, 400)

    user = CustomUser.objects.create(customer_xid=customer_xid)

    # Assuming authentication is successful, generate tokens
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return response_util.response_wrapper({"token":access_token}, status=201)