from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


    def __str__(self):
        return self.slug


class Character(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    prompt_instruction = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/character_images', blank=True, null=True)
    user = models.ForeignKey(User, related_name='character', on_delete=models.CASCADE)
    slug = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='character', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __str__(self):
       return self.slug
