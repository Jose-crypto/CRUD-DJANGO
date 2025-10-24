from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Taks(models.Model):
    title= models.CharField(max_length=100)
    descripcion= models.TextField(blank=True)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' - ' + self.descripcion  + ' by ' + self.user.username
    
    