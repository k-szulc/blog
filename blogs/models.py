from django.db import models


# Create your models here.
class BlogPost(models.Model):
    """A model for Post, that user will add to his blog"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation"""
        return self.title
