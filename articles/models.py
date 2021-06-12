from django.db.models.fields import related
from django.utils.timezone import make_aware
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from activity_logs.models import ActivityLog

# Create your models here.
class Article(models.Model):
  STATUSES = [
    ('draft', 'Draft'),
    ('published', 'Published')
  ]
  id = models.IntegerField(primary_key=True, unique=True, editable=False)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='articles')
  title = models.CharField(blank=False, null=False, max_length=200)
  description = models.TextField(blank=False, null=False)
  status = models.CharField(choices=STATUSES, default='draft', null=False, blank=False, max_length=50)
  publish_date = models.DateTimeField(null=True)
  creation_date = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'article'

  def __str__(self):
    return '{} created article: {}'.format(self.author.username, self.title)

  def save(self, *args, **kwargs):
    if self.status == 'published':
      self.publish_date = make_aware(datetime.now())
      
    super().save(*args, **kwargs)

  def get_likes_count(self, user=None):
    if user:
      return ActivityLog.objects.filter(activity='like', user=user, article=self.id).count()
    
    return ActivityLog.objects.filter(activity='like', article=self.id).count()