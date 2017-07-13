from django.db import models

# Create your models here.

class User_Model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.name)

class Task_Model(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User_Model, on_delete=models.CASCADE, blank=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
