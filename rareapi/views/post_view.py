from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, Comment, Author, Category
from rest_framework.decorators import action

class PostView(ViewSet):
    """Handles Requests to /posts"""
    def list(self, request):
        """Handles get requests to /posts
        Returns a serialized list of post instances"""
        posts = Post.objects.all()
        serialized = PostSerializer(posts, many = True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handles get requests to /posts/pk
        Returns a serialized object instance of post"""
        post = Post.objects.get(pk = pk)
        serialized = PostSerializer(post, many = False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests to /posts
        Returns a serialized instance of post with a 201"""
        author = Author.objects.get(user = request.auth.user)
        category = Category.objects.get(pk = request.data["category"])
        new_post = Post.objects.create(
            author = author,
            category = category,
            title = request.data['title'],
            publication_date = request.data['publication_date'],
            image_url = request.data['image_url'],
            content = request.data['content']
        )
        serialized = PostSerializer(new_post, many = False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT requests to /posts/pk
        Returns nothing with a 204."""
        category = Category.objects.get(pk = request.data['category'])
        post = Post.objects.get(pk = pk)
        post.category = category
        post.title = request.data['title']
        post.publication_date = request.data['publication_date']
        post.image_url = request.data['image_url']
        post.content = request.data['content']
        post.save()
        return Response(None, status = status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests to /posts/pk
        Returns nothing with a 204."""
        post = Post.objects.get(pk = pk)
        post.delete()
        return Response(None, status = status.HTTP_204_NO_CONTENT) 
    
    @action(methods=['post'], detail=True)
    def comment(self, request, pk):
        author = Author.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=pk)
        comment = Comment.objects.create(
            body = request.data['body'],
            author = author,
            post = post,
            date = request.data['date']
        )
        # post.comments.add(author.author_comment)
        return Response({'message': 'Comment Added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def delete_comment(self, request, pk):
        """pk is the pk of the comment, not the post
        """
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({'message': 'Comment Deleted'}, status=status.HTTP_204_NO_CONTENT)
        
class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id' , 'body' , 'author' , 'post' , 'date')

class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id' , 'full_name', 'profile_image_url')


class PostSerializer(serializers.ModelSerializer):
    post_comment = PostCommentSerializer(many=True)
    author = PostAuthorSerializer(many=False)
    class Meta:
        model = Post
        fields = ('id' , 'author' , 'category' , 'title' , 'publication_date' , 'image_url' , 'content' , 'approved' , 'post_comment')