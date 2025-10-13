from django.urls import path
from .views import *

urlpatterns = [
    path('', user_profile_view, name='user_profile'),
    path('list/', list_view, name='list_view'),
]