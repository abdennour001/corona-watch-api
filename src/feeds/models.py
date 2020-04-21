from django.db import models
from django.contrib.auth import get_user_model
from attachments.models import Attachment

# Create your models here.


class Publication(models.Model):
    """

    """
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=False)

    def __str__(self):
        return "%d, %s, %s" % (self.pk, self.title, self.publication_date.date())


class Article(Publication):
    """
    Article Model.
    """

    content = models.TextField()
    attachment = models.OneToOneField(
        Attachment,
        on_delete=models.CASCADE,
        null=True
    )
    editor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

    @property
    def owner(self):
        return self.editor


class Video(Publication):
    """
    Video Model.
    """

    description = models.TextField()
    attachment = models.OneToOneField(
        Attachment,
        on_delete=models.CASCADE,
        null=True,
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

    @property
    def owner(self):
        return self.user


class Comment(models.Model):
    """
    Comment Model.
    """

    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.content, self.comment_date)

    class Meta:
        ordering = ['comment_date']

    @property
    def owner(self):
        return self.user
