from django.db.models import F, Q
from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleQueries():
  def get_article_queryset(self, filters={}):
    try:
      article = Article.objects.get(**filters)
      return article
    except Exception as err:
      print('Error occurred in get_article_queryset: ', err)
      return Article.objects.none()

  def get_articles_queryset(self, filters={}, order_by=[]):
    try:
      exclude_tuple = (Q(status='draft'),)
      if filters.get('author'):
        exclude_tuple = exclude_tuple + (~Q(author=filters.get('author')),)
        del filters['author']
      
      articles = Article.objects.filter(**filters).exclude(*exclude_tuple)\
                                .order_by(*order_by)

      return articles
    except Exception as err:
      print('Error occurred in get_articles_queryset: ', err)
      return Article.objects.none()

  def get_article(self, filters={}):
    try:
      article = self.get_article_queryset(filters)
      if not 'error' in article:
        serializer = ArticleSerializer(article)
        data = serializer.data
        return {'data': data}
      return article
    except Exception as err:
      print('Error occurred in get_article: ', err)
      return {'error': 'Could not retrieve article'}

  def get_articles(self, filters={}, order_by=[]):
    try:
      articles = self.get_articles_queryset(filters, order_by)
      if not 'error' in articles:
        serializer = ArticleSerializer(articles, many=True)
        data = serializer.data
        return {'data': data}
      return articles
    except Exception as err:
      print('Error occurred in get_articles: ', err)
      return {'error': 'Could not retrieve articles'}

  def get_articles_categories(self, articles=None):
    try:
      articles = articles if articles else Article.objects.all()
      categories = articles.annotate(category_title=F('category__title'))\
                          .values('category_title').distinct()
      return categories
    except Exception as err:
      print('Error occurred in get_used_categories: ', err)
      return {'error': 'Could not retrieve categories'}

  def get_articles_statuses(self, articles=None):
    return articles.values('status').distinct()
