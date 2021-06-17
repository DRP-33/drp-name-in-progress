from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,\
 authentication_classes, permission_classes
 
from .models import Task
from utils import is_valid_request
# Create your views here.

#task types are:
#'PC': Phone Call
#'SP': Supplies
#'OT': Others
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_task(request):
  required_fields = ['description', 'date', 'task_type']
  request_data = request.POST

  if not is_valid_request(request_data, required_fields):
    return HttpResponse("missing data", status=400)

  task = Task()
  task.requestor_id = request.user.id
  task.description = request_data["description"]
  task.date = request_data["date"]
  task.t_type = request_data["task_type"]

  
  if "acceptor_id" in request_data:
    task.acceptor_id = request_data["acceptor_id"]
  if "title" in request_data:
    task.title = request_data["title"]
  if "phone_number" in request_data:
    task.phone_number = request_data["phone_number"]
  if "store_addr" in request_data:
    task.store_addr = request_data["store_addr"]
  if "delivery_addr" in request_data:
    task.delivery_addr = request_data["delivery_addr"]
  if "s_longitude" in request_data:
    task.s_longitude = request_data["s_longitude"]
  if "s_latitude" in request_data:
    task.s_latitude = request_data["s_latitude"]
  if "d_longitude" in request_data:
    task.d_longitude = request_data["d_longitude"]
  if "d_latitude" in request_data:
    task.d_latitude = request_data["d_latitude"]
  
  task.save()
  return HttpResponse(f"OK, id = {task.id}", status=200)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_tasks(request):
  return HttpResponse(f"{serializers.serialize('json', Task.objects.all())}", status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_task(request):
  data = request.POST
  required_data = ['task_id']

  if not is_valid_request(data, required_data):
    return HttpResponse("missing data", status=400)

  try:
    task = Task.objects.get(pk=data['task_id'])
    serialized_tasks = serializers.serialize('json', task)
    return HttpResponse(serialized_tasks, status=200)
  except Task.DoesNotExist:
    return HttpResponse("task with given id does not exist", status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_my_tasks(request):
  user_id = request.user.id
  my_tasks = Task.objects.filter(requestor_id=user_id)
  serialized_tasks = serializers.serialize('json', my_tasks)
  return HttpResponse(serialized_tasks, status=200)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_my_accepted_tasks(request):
  user_id = request.user.id
  my_tasks = Task.objects.filter(acceptor_id=user_id)
  serialized_tasks = serializers.serialize('json', my_tasks)
  return HttpResponse(serialized_tasks, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def accept_task(request):
  required_fields = ['task_id']
  request_data = request.POST

  if not is_valid_request(request_data, required_fields):
    return HttpResponse("missing data", status=400)

  id = request_data["task_id"]
  acceptor_id = request.user.id
  task = Task.objects.get(pk=id)
  task.acceptor_id = acceptor_id
  task.save()
  return HttpResponse("OK", status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cancel_task(request):
  required_fields = ['task_id']
  request_data = request.POST

  if not is_valid_request(request_data, required_fields):
    return HttpResponse("missing data", status=400)

  try:
    task = Task.objects.get(pk=request_data['task_id'])
    if task.requestor_id == request.user.id:
      task.delete()
      return HttpResponse('task deleted', status=200)
    else:
      return HttpResponse('you are not the owner of this task', status=403)
  except Task.DoesNotExist:
    return HttpResponse('not task with given id exists', status=404)