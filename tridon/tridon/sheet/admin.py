from django.contrib import admin

from .models import WorkbookFile
from .models import WorkbookEntry

# Register your models here.
admin.site.register(WorkbookFile)
admin.site.register(WorkbookEntry)
