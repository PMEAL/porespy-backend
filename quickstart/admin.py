from django.contrib import admin

# Register your models here.

from .models import GeneratorBlobs #, PoreSpyFuncs

admin.site.register(GeneratorBlobs)
# admin.site.register(PoreSpyFuncs)
