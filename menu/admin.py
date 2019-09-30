from django.contrib import admin

# Register your models here.

from .models import Clerks,Auxilliaryrecords,Clerkexperience,Menu

admin.site.register(Clerks)
admin.site.register(Auxilliaryrecords)
admin.site.register(Clerkexperience)
admin.site.register(Menu)