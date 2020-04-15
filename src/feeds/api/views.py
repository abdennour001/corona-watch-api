# generic api view

from django.db.models import Q
from rest_framework import generics
from feeds.models import Article, Video, Comment
from .serializers import ArticleSerializer, VideoSerializer, CommentSerializer
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


class ArticleRUDView(generics.RetrieveUpdateDestroyAPIView):
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


class VideoCreateView(generics.ListCreateAPIView):
    """
    Generic API View for Video.
    """
    lookup_field = 'id'
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        return queryset


class VideoRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic API View for : Retrieve, Update and Destroy Videos.
    """
    lookup_field = 'id'
    serializer_class = VideoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # queryset = Video.objects.all()

    # override base methods
    def get_queryset(self):
        return Video.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Video.objects.get(pk=pk)


class CommentCreateView(generics.ListCreateAPIView):
    """
    Generic API View for Comment.
    """
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(publication=self.kwargs.get('publication_id'))
        return queryset


class CommentRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic API View for : Retrieve, Update and Destroy Comments.
    """
    lookup_field = 'id'
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # queryset = Comment.objects.all()

    # override base methods
    def get_queryset(self):
        queryset = Comment.objects.filter(publication=self.kwargs.get('publication_id'))
        return queryset
