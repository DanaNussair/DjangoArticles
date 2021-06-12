from django.db import models

# Create your models here.
class Category(models.Model):
  id = models.IntegerField(primary_key=True, unique=True, editable=False)
  title = models.CharField(blank=False, null=False, max_length=200)
  description = models.TextField(blank=True, null=False)
  creation_date = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'category'
  
  def __str__(self):
    return 'category: {}'.format(self.title)