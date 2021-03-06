from django.http import Http404
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import MyUser
from movie.models import Comment, Movie
from movie.permissions import IsOwnerOrReadOnly
from movie.serializers.comment import CommentSerializer


class CommentAPIView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(movie_id=kwargs.get('movie_id'))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs.get('movie_id'))
        author = MyUser.objects.get(pk=request.user.pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['movie'] = movie
            serializer.validated_data['author'] = author
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):

    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, movie_id, pk):
        try:
            obj = Comment.objects.filter(movie_id=movie_id)[int(pk)-1]
            self.check_object_permissions(self.request, obj)
            return obj
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        comment = self.get_object(movie_id=kwargs.get('movie_id'), pk=kwargs.get('pk'))
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        comment = self.get_object(movie_id=kwargs.get('movie_id'), pk=kwargs.get('pk'))
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        comment = self.get_object(movie_id=kwargs.get('movie_id'), pk=kwargs.get('pk'))
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
