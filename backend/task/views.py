from django.shortcuts import render
from django.http import HttpResponse
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
  return HttpResponse(f"{Task.objects.all().values()}", status=200)

def accept_task(request):
  try:
    id = request.data["id"]
    acceptor_id = request.data["acceptor_id"]
    task = Task.objects.get(pk=id)
    task.acceptor_id = acceptor_id
    return HttpResponse("OK", status=200)
  except:
    return HttpResponse(":(", status=400)