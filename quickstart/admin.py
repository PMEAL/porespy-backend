from django.contrib import admin

# Register your models here.

from .models import Hero, PoreSpyGenerator
admin.site.register(Hero)
admin.site.register(PoreSpyGenerator)
