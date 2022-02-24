from django.urls import path
from .views import UserView


urlpatterns = [
    path('alluser/', UserView.search_user, name='alluser'),
]