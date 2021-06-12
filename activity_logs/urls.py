  
from django.urls import path
from .views import ActivityLogViews

urlpatterns = [
    path('activity_logs/create/<str:activity>/<int:article_id>', 
          ActivityLogViews.create, name='activity_log_create')
]