from django.urls import path

from .views import get_post_patch_wallet_view, get_transaction_view, post_deposit_view, post_withdrawals_view

urlpatterns = [
    path("", get_post_patch_wallet_view, name="get_post_patch_wallet_view"),
    path("transactions/", get_transaction_view, name="get_transaction_view"),
    path("deposits/", post_deposit_view,name="post_deposit_view"),
    path("withdrawals/", post_withdrawals_view ,name="post_withdrawals_view "),
]
