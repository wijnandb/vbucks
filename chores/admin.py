from django.contrib import admin

from django.contrib import admin

from .models import Chore, Type, Chore_done


admin.site.register(Chore)
admin.site.register(Type)
admin.site.register(Chore_done)