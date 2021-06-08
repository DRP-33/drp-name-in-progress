import json
import sys

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from utils import is_valid_request

@api_view(['POST'])
def create_user(request):
  data = request.POST
  required_data = ['user_name', 'user_email', 'user_password']
  if not is_valid_request(data, required_data):
    return HttpResponse("missing data", status=400)

  if User.objects.filter(email=data['user_email']).exists():
    return HttpResponse('email already in use', status = 409)

  user = User.objects.create_user(data['user_name'], data['user_email'],
    data['user_password'])
  user.save()

  token = Token.objects.create(user = user)

  response_data = {}
  response_data['id'] = user.id
  response_data['token'] = token.key

  return JsonResponse(response_data)