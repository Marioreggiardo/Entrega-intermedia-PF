from django.apps import AppConfig
from django.contrib import admin

from my_app.models import Meca, Segundo

admin.site.register(Meca)
admin.site.register(Segundo)



# Register your models here.
