import jwt
from datetime import datetime, timedelta
from .models import CustomUser
from rest_framework_simplejwt.tokens import AccessToken

def generate_access_token(customer_xid):
    # Define the payload for the JWT token
    payload = {
        # 'id': user.id,
        'customer_xid': customer_xid,
        'exp': datetime.utcnow() + timedelta(days=1)  # Set token expiration time
    }

    # Generate the JWT token
    jwt_token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')

    return jwt_token

def validate_access_token(token):
    try:
        decoded_token = jwt.decode(
            token,
            'your-secret-key',  # Use your own secret key from Django settings
            algorithms=['HS256'],
        )
        return decoded_token
    except jwt.exceptions.DecodeError:
        return None

def decode_access_token(token):
    try:
        decoded_token = AccessToken(token)
        return decoded_token
    except jwt.exceptions.DecodeError:
        return None

def get_access_token_from_header(request):
    authorization_header = request.headers.get('Authorization')

    if authorization_header.startswith('Token '):
        return authorization_header[6:]  # Extract the token part
    return None

def get_user_from_xid(customer_xid):
    return CustomUser.objects.get(customer_xid=customer_xid)

def get_user_from_user_id(user_id):
    return CustomUser.objects.get(id=user_id)

def validate_get_user_from_request(request):
    try:
        access_token = get_access_token_from_header(request)
        decoded_access_token = decode_access_token(access_token)
        user_id = decoded_access_token['user_id']
        user = get_user_from_user_id(user_id)
        return user
    except Exception as e:
        print(e)
        return None