import django
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings.dev')
django.setup()

from user.models import User
from task.models import Task
from django.contrib.auth.hashers import make_password
HASHER = 'md5'

def add_user(username, email, password, date):
  user = User()
  user.name = username
  user.email = email
  user.date = date
  user.password = make_password(password, hasher=HASHER)
  user.save()
  user.id

#task types are:
#'PC': Phone Call
#'SP': Supplies
#'OT': Others
def add_task(requestor_id, description, date, acceptor_id, task_type,
  title='', phone_number='', store_addr='', delivery_addr='', s_longitude=0.0,
  s_latitude=0.0, d_longitude=0.0, d_latitude=0.0):
  task = Task()
  task.requestor_id = requestor_id
  task.description = description
  task.date = date
  task.acceptor_id = acceptor_id
  task.t_type = task_type
  task.title = title
  task.phone_number = phone_number
  task.store_addr = store_addr
  task.delivery_addr = delivery_addr
  task.s_longitude = s_longitude
  task.s_latitude = s_latitude
  task.d_longitude = d_longitude
  task.d_latitude = d_latitude
  task.save()
  task.id