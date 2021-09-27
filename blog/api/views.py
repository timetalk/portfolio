from rest_framework import serializers
from blog.models import Post
from blog.serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_post_list_views(request, *args, **kwargs):
    list_qs = Post.objects.all()
    serializers = PostSerializers(list_qs, many=True)
    return Response(serializers.data, status=200)

@api_view(["GET"])
def api_post_detail_views(request, post_id, *args, **kwargs):
    qs = Post.objects.filter(id=post_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializers = PostSerializers(obj)
    return Response(serializers.data, status=200)