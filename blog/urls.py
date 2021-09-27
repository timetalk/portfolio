from django.urls import path
from .views import (
    home_views,
    blog_list_views
)


urlpatterns = [
    path('', home_views, name='home'),
    path('blog/', blog_list_views, name='blog'),
]
