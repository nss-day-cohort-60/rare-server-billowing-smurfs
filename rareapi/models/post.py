from django.db import models

class Post(models.Model):
    author = models.OneToOneField("Author", on_delete=models.CASCADE, related_name="author_post")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category_post")
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    image_url = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    approved = models.BooleanField(default = True)
    comments = models.ManyToManyField("Author", through="Comment")
