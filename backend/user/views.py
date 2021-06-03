from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
HASHER = 'md5'
# Create your views here.

def add_user(request):
  try:
    user = User()
    user.name = request.data["name"]
    user.email = request.data["email"]
    user.date = request.data["date"]
    user.password = make_password(request.data["password"], hasher=HASHER)
    user.save()
  except:
    return HttpResponse("Data missing", status=400)
    
  return HttpResponse(f"OK, id={user.id}", status=200)

def get_users(request):
  return HttpResponse(f"{Users.objects.all().values()}", status=200)
