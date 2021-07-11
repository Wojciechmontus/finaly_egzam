from django.contrib import admin
from Portfolio.models import Album,Image
# Register your models here.    
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
class ImageAdmin(admin.ModelAdmin):
    fields = ('owner','name','image','getImage','status','created')
    list_display= ('name','getImage','owner','created')
    readonly_fields = ('getImage','created',)

admin.site.register(Image,ImageAdmin)
admin.site.register(Album,AlbumAdmin)