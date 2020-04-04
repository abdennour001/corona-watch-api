from django.db import models

# Create your models here.


class Publication(models.Model):
    """

    """
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return "%d, %s, %s" % (self.pk, self.title, self.publication_date)


class Article(Publication):
    """

    """

    content = models.TextField()

    def __str__(self):
        super(Article, self).__str__()


class Video(Publication):
    """

    """

    description = models.TextField()

    def __str__(self):
        super(Video, self).__str__()


class Comment(models.Model):
    """

    """

    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s, %s" % (self.content, self.comment_date)
