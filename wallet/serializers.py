from rest_framework import serializers
from .models import Wallet, Transaction
from django.contrib.auth.models import User
import datetime


class WalletSerializer(serializers.ModelSerializer):  # create class to serializer model
    status = serializers.CharField(default="enabled", read_only=True)
    owned_by = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    enabled_at = serializers.DateTimeField(read_only=True, default=datetime.datetime.now())
    balance = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    wallet = serializers.PrimaryKeyRelatedField(many=False, queryset=Wallet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'wallet')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    deposited_by = serializers.UUIDField(source='transaction_by')
    deposited_at = serializers.DateTimeField(read_only=True, default=datetime.datetime.now(), source="transaction_at" )

    class Meta:
        model = Transaction
        fields = ('id','deposited_by','deposited_at','status','amount','reference_id')

class WithdrawalsSerializer(serializers.ModelSerializer):
    withdrawn_by = serializers.UUIDField(source='transaction_by')
    withdrawn_at = serializers.DateTimeField(read_only=True, default=datetime.datetime.now(), source="transaction_at")
    
    class Meta:
        model = Transaction
        fields = ('id','withdrawn_by','withdrawn_at','status','amount','reference_id')
        
