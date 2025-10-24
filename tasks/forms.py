from django.forms import ModelForm
from .models import Taks

class TaskForm(ModelForm):
    class Meta:
        model = Taks
        fields= ['title','descripcion','important']