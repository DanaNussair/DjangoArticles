from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActivityLog(models.Model):
  ACTIVITIES = [
    ('create', 'Create'),
    ('like', 'Like'),
    ('edit', 'Edit')
  ]
  id = models.IntegerField(primary_key=True, unique=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
  activity = models.CharField(choices=ACTIVITIES, blank=False, null=False, max_length=50)
  timestamp = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'activity_log'

  def __str__(self):
    return '{} activity on article: {}'.format(self.activity, self.article.title)


