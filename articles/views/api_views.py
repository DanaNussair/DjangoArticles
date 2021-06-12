from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

# Services
from ..services.queries import ArticleQueries
from ..services.commands import ArticleCommands
from ..services.common import CommonArticlesServices
# Support
from support.validator import Validator

class ArticleAPIView(APIView):
  
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

  @api_view(['POST'])
  def create_article(request):
    validator = Validator().validate(fields={
      'title': serializers.CharField(required=True, trim_whitespace=True),
      'description': serializers.CharField(required=True, trim_whitespace=True),
      'category': serializers.IntegerField(required=False)
    }, data=request.data)
    validator.is_valid(raise_exception=True)

    args = {**validator.validated_data, 'author': request.user.id, 'status': 'published'}
    article = ArticleCommands().create_article(args)
    if 'error' in article:
      return Response(article, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response(article, status=status.HTTP_201_CREATED)
  
  @api_view(['GET'])
  def list_articles(request):
    args = {'status': 'published'}
    validator = Validator().validate(fields={
      'title': serializers.CharField(required=False, trim_whitespace=True),
      'description': serializers.CharField(required=False, trim_whitespace=True),
      'category': serializers.IntegerField(required=False)
    }, data=request.data)
    if request.data:
      validator.is_valid(raise_exception=True)
      args = {**args, **validator.validated_data}

    articles = ArticleQueries().get_articles(args)
    
    if 'error' in articles:
      return Response(articles, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response(articles, status=status.HTTP_200_OK)