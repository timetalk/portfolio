from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

urlpatterns+=static(settings.STATIC_URL, static_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, static_root=settings.MEDIA_ROOT)


