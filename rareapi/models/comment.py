from django.db import models


class Comment(models.Model):
    body = models.CharField(max_length=25)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="author_comment")
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="post_comment")
    date = models.DateTimeField(auto_now=True)
