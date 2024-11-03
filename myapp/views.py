from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_user_view(request):
    print("Creating user...")
    User.objects.create(username="new_user")
    print("User creation initiated.")
    return HttpResponse("User created!")
