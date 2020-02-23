from django.contrib import admin

# Register your models here.
from .models import Trash
from .models import Recycle
from .models import Compost

admin.site.register(Trash)
admin.site.register(Recycle)
admin.site.register(Compost)


