# generic api view

from django.db.models import Q
from rest_framework import generics
from ..models import Article, Video, Comment, Publication
from .serializers import ArticleSerializer, VideoSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class ArticleCreateView(generics.ListCreateAPIView):
    """
        get:
        Return a list of all existing articles.

        post:
        Create an new article.
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
        get:
        Return the specific article.

        put:
        Update the specific article.

        delete:
        Delete the specific article.
    """
    lookup_field = 'id'
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # override base methods
    def get_queryset(self):
        return Article.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Article.objects.get(pk=pk)


class VideoCreateView(generics.ListCreateAPIView):
    """
        get:
        Return a list of all existing videos.

        post:
        Create an new video.
    """
    lookup_field = 'id'
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        return queryset


class VideoRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
        Return the specific video.

        put:
        Update the specific video.

        delete:
        Delete the specific video.
    """
    lookup_field = 'id'
    serializer_class = VideoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # override base methods
    def get_queryset(self):
        return Video.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Video.objects.get(pk=pk)


class CommentList(generics.ListAPIView):
    """
        get:
        Return a list of all existing Comments.
    """
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        return queryset


class CommentCreateView(generics.ListCreateAPIView):
    """
        get:
        Return a list of Comments of the publication with (pk=publication_id).

        post:
        Create a new Comment for the publication with ( pk=publication_id ).

    """
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(publication=self.kwargs.get('publication_id'))
        return queryset

    def perform_create(self, serializer):
        serializer.save(publication=get_object_or_404(Publication, pk=self.kwargs.get('publication_id')))


class CommentRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
            Return the comment with ( pk=id ) of the publication with ( pk=publication_id ).
        put:
            Update (if you are owner) the comment with ( pk=id ) of the publication with ( pk=publication_id ).
        delete:
            Delete (if you are owner) the comment with ( pk=id ) of the publication with ( pk=publication_id ).
    """
    lookup_field = 'id'
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # override base methods
    def get_queryset(self):
        queryset = Comment.objects.filter(publication=self.kwargs.get('publication_id'))
        return queryset
