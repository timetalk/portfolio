from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to="images/")
    timestamp = models.DateTimeField(auto_now_add=True)