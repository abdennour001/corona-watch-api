# generic api view

from django.db.models import Q
from rest_framework import generics
from feeds.models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly


class ArticleCreateView(generics.ListCreateAPIView):
    """
    Generic API View : Create Article.
    """
    lookup_field = 'id'
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return queryset

    # def perform_create(self, serializer):
    #     serializer.save(self.request.user)


class ArticleRUDView(generics.RetrieveUpdateDestroyAPIView,
                     generics.CreateAPIView):
    """
    Generic API View for : Retrieve, Update and Destroy Articles.
    """
    lookup_field = 'id'
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = Article.objects.all()

    # override base methods
    def get_queryset(self):
        return Article.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Article.objects.get(pk=pk)
