from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "DOT AP Integrated Management System"
class fileCust(admin.ModelAdmin):
    list_filter = ("date_added",)
    list_display = ("filename", "date_added")
    
admin.site.register(selectfile)


# Register your models here.
