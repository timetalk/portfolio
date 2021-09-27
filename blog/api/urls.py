from django.urls import path
from . views import (
    api_post_list_views,
    api_post_detail_views,
    )

urlpatterns = [
    path('post/', api_post_list_views),
    path('<int:post_list>/', api_post_detail_views),
]
