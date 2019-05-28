from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin

@admin.register(People)
class ViewAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
