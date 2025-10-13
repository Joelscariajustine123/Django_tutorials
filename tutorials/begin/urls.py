from django.urls import path

from begin.views import *

urlpatterns = [
    path('', home, name='home'),
    path('second/', second, name='second'),
    path('user_details/', user_details, name='user_details'),
    path('third/', third, name='third'),
]