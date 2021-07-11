from django.db import models
from django.utils.html import format_html

class Album(models.Model):
    name = models.CharField(max_length=150, verbose_name="Album")
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("name", )
    def __str__(self):
        return self.name

class Image(models.Model):
    STATUS_CHOICE = (
        ("activa", "Activa"),
        ("inactiva", "Inactiva"),
    )
    owner = models.ForeignKey(Album, on_delete= models.CASCADE, verbose_name="Album")
    id = models.AutoField(null=False, primary_key = True, unique = True)
    image = models.ImageField(upload_to="portfolio",verbose_name="Seleccione imagen")
    name = models.CharField(max_length=100,verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creada")
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICE,
                            default="inactiva",
                            verbose_name="Estado")
    
    def getImage(self):
        if self.image:
            return format_html("<img src='{}' style='width:120px; height:100px;' >",self.image.url)
        else:
            return 'Sin imagen previa'
    getImage.short_description = 'Imagen previa'
    getImage.allow_tags = True
    
    class Meta:
        ordering =("-id",)
    def __str__(self):
        return self.name