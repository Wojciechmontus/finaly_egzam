from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Empresa(models.Model):
    
    image = models.ImageField(upload_to = "img",verbose_name = "Imagen")
    title = models.CharField(max_length=250,verbose_name="Título")    
    content = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.title

    