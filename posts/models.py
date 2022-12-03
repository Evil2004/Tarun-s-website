from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = 'post'
