from django.contrib import admin

# Register your models here.
from . models import Place, Teams

admin.site.register(Place)
admin.site.register(Teams)