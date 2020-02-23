from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recycle
from .models import Trash
from .models import Compost

def index(request):
    all_recycle = Recycle.objects.all()
    all_trash = Trash.objects.all()
    all_compost = Compost.objects.all()
    template = loader.get_template('sortingCans/index.html')
    context = {
        'all_recycle': all_recycle,
        'all_trash' : all_trash,
        'all_compost' : all_compost,
    }
    return HttpResponse(template.render(context,request))



# Create your views here.
