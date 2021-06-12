from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleCommands():
  def create_article(self, args={}):
    try:
      serializer = ArticleSerializer(data=args)
      if serializer.is_valid():
        serializer.save()
        return {'data': serializer.data}
      else:
        print("Errors: ", serializer.errors)
        return {'error': 'Provided parameters are incorrect'}
    except Exception as err:
      print('Error occurred in create_article', err)
      return {'error': 'Could not create article'}

  def update_article(self, pk, update_data={}):
    try:
      article = Article.objects.get(id=pk)
      serializer = ArticleSerializer(article, data=update_data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return {'data': serializer.data}
      else:
        return {'error': 'Provided parameters are incorrect'}
    except Exception as err:
      print('Error occurred in update_article', err)
      return {'error': 'Could not update article'}

  def delete_article(self, pk):
    try:
      article = Article.objects.get(id=pk, status='draft')

      if article.delete():
        return {'data': 'Successfully deleted.'}
      else:
        return {'error': 'Provided parameters are incorrect'}
    except Exception as err:
      print('Error occurred in delete_article', err)
      return {'error': 'Could not delete article'}
