  
from django.urls import path
from .views.template_views import ArticlesTemplateView
from .views.api_views import ArticleAPIView

urlpatterns = [
    path('', ArticlesTemplateView.home, name='home'),
    path('articles/', ArticlesTemplateView.articles, name='articles'),
    path('articles/create', ArticlesTemplateView.create, name='articles_create'),
    path('articles/list_articles', ArticleAPIView.list_articles, name='articles_api_list'),
    path('articles/create_article', ArticleAPIView.create_article, name='articles_api_create'),
    path('articles/<int:pk>/edit', ArticlesTemplateView.edit, name='articles_edit'),
    path('articles/<int:pk>/delete', ArticlesTemplateView.delete, name='articles_delete'),
]