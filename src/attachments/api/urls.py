from django.urls import path
from .views import AttachmentListView

urlpatterns = [
    # attachments urls
    path('', AttachmentListView.as_view(), name='attachment-list'),
]
