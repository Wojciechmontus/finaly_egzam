from django.contrib import admin
from empresa import models

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("title","image")
admin.site.register(models.Empresa,EmpresaAdmin)