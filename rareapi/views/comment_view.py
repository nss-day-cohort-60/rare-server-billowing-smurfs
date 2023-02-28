from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Author, Comment, Post


class CommentView(ViewSet):
    def list(self, request):

        comments = Comment.objects.all()

        if "post_id" in request.query_params:
            post = Post.objects.get(pk=request.query_params["post_id"])
            comments = comments.filter(post=post)

        for comment in comments:
            comment.is_author = False
            if comment.author.user == request.auth.user:
                comment.is_author = True

        serialized = CommentSerializer(comments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class CommentAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'username', 'profile_image_url')


class CommentSerializer(serializers.ModelSerializer):
    author = CommentAuthorSerializer(many=False)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'post', 'date', 'is_author')
