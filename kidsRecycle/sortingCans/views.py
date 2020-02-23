from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recycle

def index(request):
    all_recycle = Recycle.objects.all()
    template = loader.get_template('sortingCans/index.html')
    context = {
        'all_recycle': all_recycle,
    }
    return HttpResponse(template.render(context,request))



# Create your views here.
