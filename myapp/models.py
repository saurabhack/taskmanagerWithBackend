from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=100)
    details=RichTextField(blank=True,null=True)
    date=models.DateTimeField(default=timezone.now)
    startingTime=models.TimeField(default=timezone.now)
    finishingTime=models.TimeField(default=timezone.now)
    def __str__(self):
        return self.title


