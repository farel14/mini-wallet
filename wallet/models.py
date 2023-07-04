from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.models import CustomUser
import uuid
from django.core.validators import MinValueValidator

# Create your models here.
class Wallet(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False
         )
    owned_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="enabled")
    enabled_at = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField(default=0)

class Transaction(models.Model):
    class TransactionStatus(models.TextChoices):
        SUCCESS = "success", _("Success")
        FAILED = "failed", _("Failed")
    class TransactionType(models.TextChoices):
        DEPOSIT = "deposit", _("Deposit")
        WITHDRAWAL = "withdrawal", _("Withdrawal")
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False
         )
    transaction_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        choices=TransactionStatus.choices,
        default=TransactionStatus.SUCCESS,
        max_length=100
    )
    type = models.CharField(
        choices=TransactionType.choices,
        default=TransactionType.WITHDRAWAL,
        max_length=100
    )
    transaction_at= models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    reference_id = models.UUIDField(unique=True)





