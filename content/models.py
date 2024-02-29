from django.db import models
from province.models import Province

# Create your models here.
class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField()
    content_type = models.CharField(max_length=20)
    province = models.ForeignKey(Province, related_name='contents' , null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
