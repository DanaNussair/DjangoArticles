from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from rest_framework import serializers

# Services
from ..services.queries import ArticleQueries
from ..services.commands import ArticleCommands
from ..services.common import CommonArticlesServices
from categories.services.queries import CategoryQueries
# Support
from support.validator import Validator

class ArticlesTemplateView():
  def home(request):
    return render(request, 'articles/home.html')

  def articles(request):
    message = None
    filters = {'author': request.user.id} if request.user.id else {}
    order_by = {}
    if request.GET.get('deletion_success') == 'True':
      message = 'Deleted Article Successfully' 

    if request.GET:
      filter_validator = Validator().validate(fields={
        'title': serializers.CharField(required=False, trim_whitespace=True),
        'description': serializers.CharField(required=False, trim_whitespace=True),
        'category_title': serializers.CharField(required=False),
        'status': serializers.ChoiceField(required=False, choices=['draft', 'published'])
      }, data=request.GET)
      if filter_validator.is_valid():
        filters = {**filters, **filter_validator.validated_data}
      else:
        message = "Invalid filtering parameters"
      
      order_validator = Validator().validate(fields={
        'sort_by': serializers.CharField(required=False)
      }, data=request.GET)
      if order_validator.is_valid():
        order_by = order_validator.validated_data
      else:
        message = "Invalid sorting parameters"

    filters = CommonArticlesServices().handle_args(filters)
    order_by = CommonArticlesServices().handle_order_by(order_by)

    articles = ArticleQueries().get_articles_queryset(filters, order_by)
    if not 'error' in articles:
      categories = ArticleQueries().get_articles_categories(articles)
      statuses = ArticleQueries().get_articles_statuses(articles)
      if len(articles) == 0:
        message = 'No Articles Found.'

    return render(request, 'articles/articles.html', {'title': 'Articles', 'message': message
        , 'articles': articles, 'categories': categories, 'statuses': statuses})

  def create(request):
    is_authenticated = request.user.is_authenticated
    message = None
    categories = CategoryQueries().get_categories_queryset() if is_authenticated else []

    if is_authenticated and request.POST:
      validator = Validator().validate(fields={
        'title': serializers.CharField(required=True, trim_whitespace=True),
        'description': serializers.CharField(required=True, trim_whitespace=True),
        'category': serializers.IntegerField(required=False)
      }, data=request.POST)
      if validator.is_valid():
        args = {**validator.validated_data, 'author': request.user.id}
        created = ArticleCommands().create_article(args)

        if 'data' in created:
          return redirect('articles')
        else:
          message = "Can not create article"
      else:
        message = "Invalid parameters"

    return render(request, 'articles/create_article.html', 
      {'title': 'Create Article', 'message': message, 'categories': categories})
  
  def edit(request, pk=None):
    article = ArticleQueries().get_article_queryset({'id': pk})
    is_author_logged_in = request.user.username == article.author.username
    message = None
    args = {}
    if not is_author_logged_in:
      message = "You do not have permission to edit this article"
    elif request.POST:
      validator = Validator().validate(fields={
        'title': serializers.CharField(required=False, trim_whitespace=True),
        'description': serializers.CharField(required=False, trim_whitespace=True),
        'status': serializers.ChoiceField(required=False, choices=['draft', 'published'])
      }, data=request.POST)
      if validator.is_valid():
        args = validator.validated_data
        updated = ArticleCommands().update_article(pk=pk, update_data=args)
        if 'data' in updated:
          return redirect('articles')
        else:
          message = "Could not update article"
      else:
        message = "Invalid parameters"
    
    return render(request, 'articles/edit_article.html', 
      {'title': 'Edit Article', 'article': article, 'message': message})

  def delete(request, pk=None):      
    article = ArticleQueries().get_article_queryset({'id': pk})
    deletion_success = False
    if article and request.user.username == article.author.username:
      deleted = ArticleCommands().delete_article(pk=pk)
      if 'data' in deleted:
        deletion_success = True
    
    base_url = reverse('articles')
    query_string = urlencode({'deletion_success': deletion_success})
    url = "{}?{}".format(base_url, query_string)
    
    return redirect(url)