from django.urls import path
from .views import init_user_view

urlpatterns = [
    path('', init_user_view, name='init_user'),
]