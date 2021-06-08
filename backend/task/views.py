from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,\
 authentication_classes, permission_classes
from .models import Task
# Create your views here.

#task types are:
#'PC': Phone Call
#'SP': Supplies
#'OT': Others
def add_task(request):
  try:
    task = Task()
    task.requestor_id = request.data["requestor_id"]
    task.description = request.data["description"]
    task.date = request.data["date"]
    task.t_type = request.data["task_type"]
  except:
    return HttpResponse("missing data", status=400)
  
  if "acceptor_id" in request.data:
    task.acceptor_id = request.data["acceptor_id"]
  if "title" in request.data:
    task.title = request.data["title"]
  if "phone_number" in request.data:
    task.phone_number = request.data["phone_number"]
  if "store_addr" in request.data:
    task.store_addr = request.data["store_addr"]
  if "delivery_addr" in request.data:
    task.delivery_addr = request.data["delivery_addr"]
  if "s_longitude" in request.data:
    task.s_longitude = request.data["s_longitude"]
  if "s_latitude" in request.data:
    task.s_latitude = request.data["s_latitude"]
  if "d_longitude" in request.data:
    task.d_longitude = request.data["d_longitude"]
  if "d_latitude" in request.data:
    task.d_latitude = request.data["d_latitude"]
  
  task.save()
  return HttpResponse(f"OK, id = {task.id}", status=200)

def get_tasks(request):
  return HttpResponse(f"{serializers.serialize('json', Task.objects.all())}", status=200)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_my_tasks(request):
  user_id = Token.objects.get(key=request.token).user_id
  my_tasks = Task.objects.filter(acceptor_id=user_id)
  serialized_tasks = serializers.serialize('json', my_tasks)
  return HttpResponse(serialized_tasks, status=200)

def accept_task(request):
  try:
    id = request.POST["id"]
    acceptor_id = request.POST["acceptor_id"]
    task = Task.objects.get(pk=id)
    task.acceptor_id = acceptor_id
    return HttpResponse("OK", status=200)
  except:
    return HttpResponse(":(", status=400)