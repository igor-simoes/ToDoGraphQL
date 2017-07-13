from django.contrib import admin
from .models import Task_Model, User_Model


# Register your models here.
admin.site.register(User_Model)
admin.site.register(Task_Model)