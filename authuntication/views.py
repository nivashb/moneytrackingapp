from django.shortcuts import render
from django.views import View


# Create your views here.

class login(View):
    def get(self, request):
        return render(request, 'authuntication/login.html')
