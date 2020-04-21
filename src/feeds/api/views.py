# generic api view

from django.db.models import Q
from rest_framework import generics, views, status
from rest_framework.response import Response
from ..models import Article, Video, Comment, Publication
from .serializers import ArticleSerializer, \
    VideoSerializer, \
    CommentSerializer, \
    ArticleUpdateSerializer, \
    VideoUpdateSerializer, PublicationSerializer
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404, Http404


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


class ArticleRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
        get:
        Return the specific article.

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


class ArticleUpdateView(generics.RetrieveUpdateAPIView):
    """
        put:
        Update the specific article.

        patch:
        Update the article partial update.
    """
    lookup_field = 'id'
    serializer_class = ArticleUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # override base methods
    def get_queryset(self):
        return Article.objects.all()


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


class VideoRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
        Return the specific video.

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


class VideoUpdateView(generics.RetrieveUpdateAPIView):
    """
    put:
    Update the specific video.

    patch:
    Update the video partial update.
    """
    lookup_field = 'id'
    serializer_class = VideoUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # override base methods
    def get_queryset(self):
        return Video.objects.all()


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


class PublicationsList(generics.ListAPIView):
    """
    get:
    Get list of all publications.
    """
    lookup_field = 'id'
    serializer_class = PublicationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Publication.objects.all()


class ValidatePublication(views.APIView):
    """
    Validate the publication with ( pk='publication_id' ).
    """
    permission_classes = (IsOwnerOrReadOnly,)

    def get_publication(self, publication_id):
        try:
            publication = Publication.objects.get(pk=publication_id)
        except Publication.DoesNotExist:
            raise Http404
        pass
        return publication

    def put(self, request, publication_id):
        publication = self.get_publication(publication_id)
        publication.is_validated = not publication.is_validated
        publication.save()
        return Response(status=status.HTTP_201_CREATED)
