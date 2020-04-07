from django.urls import path
from .views import ArticleRUDView, ArticleCreateView


urlpatterns = [
    path('articles/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<id>/', ArticleRUDView.as_view(), name='article-rud')
]
