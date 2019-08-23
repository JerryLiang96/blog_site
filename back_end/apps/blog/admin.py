from django.contrib import admin
from . import models
from .models import Blog
# Register your models here.

admin.site.register(models.Blog)

admin.site.register(models.Category)

admin.site.register(models.Tag)
