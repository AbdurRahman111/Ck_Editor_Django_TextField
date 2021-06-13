from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Blogs(models.Model):
    Title = models.CharField(max_length=2000)
    Details = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.Title
