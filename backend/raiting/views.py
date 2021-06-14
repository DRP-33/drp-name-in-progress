from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,\
 authentication_classes, permission_classes

from .models import Raiting
from utils import is_valid_request

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_raiting(request):
  required_fields = ['id']
  request_data = request.POST
  
  if not is_valid_request(request_data, required_fields):
    return HttpResponse("missing data", status=400)

  raiting = get_or_create_user_raiting(request_data['id'])

  serialized_raiting = serializers.serialize('json', raiting)
  return HttpResponse(serialized_raiting, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_user_raiting(request):
  required_fields = ['scored_id', 'score']
  request_data = request.POST

  if not is_valid_request(request_data, required_fields):
    return HttpResponse("missing data", status=400)

  if request_data['score'] > 5 or request_data['score'] < 0:
    return HttpResponse("invalid score value", status=400)

  user_id = request.user.id
  raiting = get_or_create_user_raiting(user_id)

  if raiting.r_count == 0:
    raiting.r_score = request_data['score']
  else:
    count = raiting.r_count
    new_score = (raiting.r_score * count + request_data['score']) / (count + 1)
    raiting.r_score = new_score
  
  raiting.r_count += 1

  raiting.save()

  serialized_raiting = serializers.serialize('json', raiting)
  return HttpResponse(serialized_raiting, status=200)


def get_or_create_user_raiting(user_id):
  try:
    raiting = Raiting.objects.get(user_id=user_id)
  except Raiting.DoesNotExist:
    raiting = Raiting()
    raiting.user_id = user_id
    raiting.r_count = 0
    raiting.r_score = 0.0
    raiting.save()
  
  return raiting