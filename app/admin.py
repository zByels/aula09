from django.contrib import admin
from . import models
from app.models import Post

# Register your models here.
admin.site.register(Post)