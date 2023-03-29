from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=228)
    body = models.TextField()
    image = models.ImageField(upload_to='posts_generic/', null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        if self.image:
            return f"http://127.0.0.1:8000{self.image.url}"
        return None
