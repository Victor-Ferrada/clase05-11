
from django.contrib import admin
from django.urls import path
from django.conf import settings
from noticia import views

urlpatterns = [
    path("lista/", views.lista,name='lista'),
    path("category/<int:category_id>/",views.category,name='category'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
