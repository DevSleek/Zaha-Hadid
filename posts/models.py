from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='media/photos', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic']),])
    description = RichTextField()

    teaching_category = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
    

class Job(models.Model):
    title = models.CharField(max_length=256)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')

    options = models.ManyToManyField('Option', related_name='jobs', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Option(models.Model):
    title = models.CharField(max_length=256)
    value = models.CharField(max_length=256)

    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title


