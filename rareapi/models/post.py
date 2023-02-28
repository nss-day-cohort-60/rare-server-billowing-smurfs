from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="author_post")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category_post")
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    approved = models.BooleanField(default=True)

    @property
    def is_author(self):
        return self.__author

    @is_author.setter
    def is_author(self, value):
        self.__author = value

    @property
    def author_comments(self):
        return self.__author

    @author_comments.setter
    def author_comments(self, value):
        self.__author = value
