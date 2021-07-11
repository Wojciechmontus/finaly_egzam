from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Anuncio(models.Model):
    STATUS_CHOICES = (
        ('borrador','Borrador'),
        ('publicado','Publicado')
    )
    title = models.CharField(max_length=250,verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    author = models.CharField(max_length=250,verbose_name="Autor")
    image = models.ImageField(upload_to="img",verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Última actualización")
    status = models.CharField(
        max_length = 10,
        choices=STATUS_CHOICES,
        default='borrador',
        verbose_name='Estado'
    )

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title