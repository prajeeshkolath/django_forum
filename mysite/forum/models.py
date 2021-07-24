"""User Model"""
import uuid

from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    title  = models.CharField(max_length=100, editable=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'forum_category'


class Topic(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    title  = models.CharField(max_length=100, editable=True)
    description  = models.TextField(editable=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='topics')

    @cached_property
    def num_of_threads(self):
        return self.thread_set.all().count()

    @cached_property
    def latest_post(self):
        return Post.objects.select_related('user_id').\
            filter(thread__topic__id=self.id).order_by('-created_at').first()

    class Meta:
        db_table = 'forum_topic'


class Thread(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    subject  = models.CharField(max_length=100, editable=True)
    created_at = models.DateTimeField( auto_now_add=True, editable=False, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'forum_thread'


class Post(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    content  = models.TextField(editable=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField( auto_now_add=True, editable=False, null=False, blank=False)
    parent_post = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'forum_post'