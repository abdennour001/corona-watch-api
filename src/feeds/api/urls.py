from django.urls import path
from .views import ArticleRetrieveDeleteView, \
    ArticleUpdateView, \
    ArticleCreateView, \
    VideoCreateView, \
    VideoRetrieveDeleteView, \
    VideoUpdateView, \
    CommentCreateView, \
    CommentRUDView, \
    CommentList, \
    ValidatePublication, PublicationsList


urlpatterns = [
    # publications urls
    path('publications/', PublicationsList.as_view(), name='publication-list'),
    path('publications/validate/<publication_id>', ValidatePublication.as_view(), name='publication-validate'),


    # articles urls
    path('articles/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<id>/', ArticleRetrieveDeleteView.as_view(), name='article-rd'),
    path('articles/update/<id>', ArticleUpdateView.as_view(), name='article-update'),

    # videos urls
    path('videos/', VideoCreateView.as_view(), name='video-create'),
    path('videos/<id>/', VideoRetrieveDeleteView.as_view(), name='video-rd'),
    path('videos/update/<id>/', VideoUpdateView.as_view(), name='video-update'),

    # comments urls
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('<publication_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('<publication_id>/comments/<id>/', CommentRUDView.as_view(), name='comment-rud'),
]
