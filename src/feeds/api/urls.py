from django.urls import path
from .views import ArticleRUDView, ArticleCreateView, VideoCreateView, VideoRUDView, CommentCreateView, CommentRUDView


urlpatterns = [
    path('articles/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<id>/', ArticleRUDView.as_view(), name='article-rud'),
    path('videos/', VideoCreateView.as_view(), name='video-create'),
    path('videos/<id>/', VideoRUDView.as_view(), name='video-rud'),
    path('<publication_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('<publication_id>/comments/<id>/', CommentRUDView.as_view(), name='comment-rud'),
]
