from django.shortcuts import render
from django.http import HttpResponse

from user.models import UserModel


class UserView():

    def search_user(self):
        user = UserModel.objects.all()
        print(user)
        return HttpResponse(f'Informações dos usuarios: {user}')

