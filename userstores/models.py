from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):

    user= models.OneToOneField(User, on_delete= models.CASCADE, related_name='user')
    location = models.TextField(max_length=30, blank=True)
    bio = models.TextField(max_length= 200)
    


class Store(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    name= models.CharField(max_length=200)
    slug = models.SlugField(default='',blank=True,  null=False, db_index=True)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store')
    title = models.TextField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True,blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.title


class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=20)
    description = models.TextField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.title

    