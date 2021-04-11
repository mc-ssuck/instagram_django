from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=100, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(upload_to='images/%Y/%m/%d/',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    hashtags = models.ManyToManyField(Hashtag, related_name='posts', blank=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

