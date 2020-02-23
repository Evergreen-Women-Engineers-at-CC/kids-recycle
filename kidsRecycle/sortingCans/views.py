from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recycle
from .models import Trash
from .models import Compost

def getpic(self):
    return
def index(request):
    all_recycle = Recycle.objects.all()
    all_trash = Trash.objects.all()
    compost = Compost.objects.all()

    #this is what we were able to render in the view
    thing = Compost.objects.get(id=2)
    compost_pic = thing.filepath


    template = loader.get_template('sortingCans/index.html')
    context = {
        'all_recycle': all_recycle,
        'all_trash' : all_trash,
        'compost' : compost,
        'thing' : thing,
        #dictionary definition sending "context" to the template
        'compost_pic' : thing
    }
    return HttpResponse(template.render(context,request))



# Create your views here.
