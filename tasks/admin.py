from django.contrib import admin
from .models import Taks
# Register your models here.

class Taskadmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    

admin.site.register(Taks,Taskadmin)
