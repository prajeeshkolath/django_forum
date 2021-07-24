from django.contrib import admin

# Register your models here.
from .models import Category, Topic, Thread, Post

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Thread)
admin.site.register(Post)