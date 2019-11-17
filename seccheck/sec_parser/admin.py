from django.contrib import admin
from sec_parser.models import Index

# Register your models here.

class IndexAdmin(admin.ModelAdmin):
    pass
admin.site.register(Index, IndexAdmin)