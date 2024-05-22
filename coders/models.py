from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class Postblog(models.Model):
    Title = models.CharField(max_length=100)
    Desc = FroalaField()
    # Desc = models.TextField()
    author = models.CharField(max_length=130)
    image = models.ImageField(upload_to="images/")
    slug = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Title
    
class comments(models.Model):
    comments = models.CharField(max_length = 500)