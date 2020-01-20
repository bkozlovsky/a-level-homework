from django.contrib import admin
from .models import Animal, Ticket, Visit, Visitor

# Register your models here.

admin.site.register(Animal)
admin.site.register(Visitor)
admin.site.register(Ticket)
admin.site.register(Visit)