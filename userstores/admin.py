from django.contrib import admin
from .models import Profile, Store, Product, Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Comment)
