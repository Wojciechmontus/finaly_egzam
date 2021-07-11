from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.home,name = 'home'),
    path('',include('anuncios.urls')),
    path('',include('sendmail.urls')),
    path('',include('empresa.urls')),
    path('',include('Portfolio.urls')),
]


# para servir ficheros estaticos 
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

