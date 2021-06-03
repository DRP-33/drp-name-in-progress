from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
HASHER = 'md5'
# Create your views here.
@csrf_protect
def add_user(request):
  try:
    user = User()
    user.name = request.data["name"]
    user.email = request.data["email"]
    user.password = make_password(request.data["password"], hasher=HASHER)
    user.save()
  except:
    return HttpResponse("Data missing", status=400)
    
  return HttpResponse(f"OK, id={user.id}", status=200)

def get_users(request):
  return HttpResponse(f"{serializers.serialize('json', User.objects.all())}", status=200)
