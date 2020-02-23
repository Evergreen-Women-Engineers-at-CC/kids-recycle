from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models.aggregates import Count
from random import randint
from .models import Recycle
from .models import Trash
from .models import Compost


def index(request):
    all_recycle = Recycle.objects.all()
    all_trash = Trash.objects.all()
    compost = Compost.objects.all()
    thing = Compost.objects.get(id=2)

    #number_of_compost = Compost.objects.count()
    #random_index = int(random.random()*number_of_compost)+1
#    random_compost = Compost.get(pk= random_index)
    random_compost = Compost.objects.order_by('?').first()

    template = loader.get_template('sortingCans/index.html')
    context = {
        'all_recycle': all_recycle,
        'all_trash' : all_trash,
        'compost' : compost,
        'random_compost' : random_compost,
        'thing' : thing
    }
    return HttpResponse(template.render(context,request))



# Create your views here.
