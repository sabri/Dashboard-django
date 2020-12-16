from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Desktop,Laptop)
class ViewAdmin(ImportExportModelAdmin):  #############admin.ModelAdmin:paramétre aprés import_export
    pass