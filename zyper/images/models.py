from django.db import models
from django.utils import timezone

# Create your models here.
class ImageFile(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    file_original = models.FileField()
    file_thumb = models.FileField(null=True)
