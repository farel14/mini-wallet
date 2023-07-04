from rest_framework.decorators import api_view, authentication_classes, permission_classes
from mini_wallet.response_util import response_wrapper
from authentication.authorization import validate_get_user_from_request
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer, DepositSerializer, WithdrawalsSerializer
from mini_wallet.utils import parse_bool

@api_view(['GET','POST', 'PATCH'])
def get_post_patch_wallet_view(request):
    user = validate_get_user_from_request(request)
    
    if not user:
        return response_wrapper("Unauthorized", 401)

    if request.method == 'GET':
        wallet_obj = Wallet.objects.get(owned_by=user)
        # check for wallet status
        if wallet_obj.status != 'enabled':
            return response_wrapper("Wallet disabled", 404)
        serializer = WalletSerializer(instance=wallet_obj)
        return response_wrapper(serializer.data, 200)
    elif request.method == 'POST':
        [wallet_obj] = Wallet.objects.get_or_create(status="enabled", owned_by=user)
        if wallet_obj.status == 'enabled':
            return response_wrapper("Already enabled", 404)
        serializer = WalletSerializer(instance=wallet_obj)
        return response_wrapper(serializer.data, 201)
    elif request.method == 'PATCH':
        # parse input
        is_disabled = request.data.get('is_disabled')
        if not is_disabled:
            return response_wrapper("Already disabled", status=400)
        is_disabled_bool = parse_bool(is_disabled)
        # get wallet
        wallet_obj = Wallet.objects.get(owned_by=user)
        # update wallet
        wallet_obj.status = "disabled" if is_disabled_bool else "enabled"
        wallet_obj.save()
        serializer = WalletSerializer(instance=wallet_obj)
        return response_wrapper(serializer.data, 200)
    # return response_wrapper("", 500)

@api_view(['GET'])
def get_transaction_view(request):
    user = validate_get_user_from_request(request)
    
    if not user:
        return response_wrapper("Unauthorized", 401)
    trasaction_list = Transaction.objects.filter(transaction_by_id= user.id)
    return response_wrapper(trasaction_list, 200)

@api_view(['POST'])
def post_deposit_view(request):
    user = validate_get_user_from_request(request)
    amount_str = request.data.get('amount')
    reference_id = request.data.get('reference_id')
    amount_int = int(amount_str)
    
    if not user:
        return response_wrapper("Unauthorized", 401)
    trasaction_obj = Transaction.objects.create(reference_id=reference_id, type="deposit", amount=amount_int, transaction_by_id=user.id)
    # adjust balance
    wallet_obj = Wallet.objects.get(owned_by=user)
    # update wallet
    wallet_obj.balance += amount_int
    wallet_obj.save()
    serializer = DepositSerializer(instance=trasaction_obj)
    return response_wrapper({"deposit": serializer.data}, 201)

@api_view(['POST'])
def post_withdrawals_view(request):
    user = validate_get_user_from_request(request)
    amount_str = request.data.get('amount')
    reference_id = request.data.get('reference_id')
    amount_int = int(amount_str)
    
    if not user:
        return response_wrapper("Unauthorized", 401)
    wallet_obj = Wallet.objects.get(owned_by=user)
    # adjust balance
    wallet_obj.balance -= amount_int
    if wallet_obj.balance < 0:
        return response_wrapper({"balance": [
        "Balance cannot be less than zero."
      ]}, 400)
    trasaction_obj = Transaction.objects.create(reference_id=reference_id, type="withdrawal", amount=amount_int, transaction_by_id=user.id)
    # update wallet
    wallet_obj.save()
    serializer = WithdrawalsSerializer(instance=trasaction_obj)
    return response_wrapper({"withdrawal": serializer.data}, 201)
