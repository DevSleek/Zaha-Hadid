from django.db import models

# Create your models here
class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
    

class SubCategory(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True
    )

    def __str__(self):
        return self.title
    

class Values(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='values')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='values', null=True, blank=True)
    value = models.CharField(max_length=256)
    

    def __str__(self):
        return self.category.title
    

class Archive(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='archives')
    main_photo = models.ImageField(blank=True, null=True, editable=False)
    is_video = models.BooleanField(default=False)


class Photo(models.Model):
    image = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, related_name='photos')
    is_main = models.BooleanField(default=False)


    @classmethod
    def get_main_photo(cls, archive_id):
        photo = Photo.objects.filter(archive_id=archive_id, is_main=True).first()
        print(photo)
        if photo:
            return photo.image
        return None
    
    def __str__(self):
        return f'{self.archive.title} photos'
    

class Video(models.Model):
    video = models.FileField(upload_to='media/videos/', null=True, blank=True)
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, related_name='videos')
    
    def __str__(self):
        return f'{self.archive.title} videos'