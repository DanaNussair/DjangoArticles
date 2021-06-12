from django import template
from activity_logs.services.queries import ActivityLogQueries
from articles.services.queries import ArticleQueries

register = template.Library()

@register.filter(name="is_author")
def is_author(article, user):
  return user.username == article.author.username

@register.filter(name="check_user_likes")
def check_user_likes(article, user):
  args = {
    'activity': 'like',
    'article': article,
    'user': user
  }

  return ActivityLogQueries().get_activities(args).count()

@register.filter(name="can_delete")
def can_delete(article):
  args = {
    'id': article.id,
    'status': 'draft'
  }

  return ArticleQueries().get_article_queryset(args)

@register.filter(name="check_if_published")
def check_if_published(article):
  args = {
    'status': 'published',
    'id': article.id
  }

  return not ArticleQueries().get_article_queryset(args)