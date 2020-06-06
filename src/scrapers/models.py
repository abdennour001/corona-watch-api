from django.db import models
from rest_framework.reverse import reverse as api_reverse


# Create your models here.


class YoutubeVideo(models.Model):
    """
        Youtube video
    """
    video_embed_url = models.URLField()
    video_id = models.CharField(max_length=256)
    published_at = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    channel_title = models.CharField(max_length=512)
    description = models.TextField()
    is_validated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.title, self.is_validated)

    def get_api_url(self, request=None):
        return api_reverse("api-feeds:article-rd", kwargs={'id': self.pk}, request=request)
