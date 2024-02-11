from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from blog.views import index, detalles,  caseros, packs
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


urlpatterns = [
    path('sherklan/', admin.site.urls),
    path('', index , name='index'),
    path('caseros/', caseros, name='caseros'),
    path('packs', packs , name='packs'),
    path('detalles/<int:detalles>', detalles, name='detalles'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() # new
