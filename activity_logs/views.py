from django.shortcuts import redirect
from rest_framework import serializers

# Services
from activity_logs.services.commands import ActivityLogCommands
from activity_logs.services.queries import ActivityLogQueries
# Support
from support.validator import Validator

class ActivityLogViews():
  def create(request, activity, article_id):
    args = {'activity': activity, 'article': article_id, 'user': request.user.id}
    validator = Validator.validate(fields={
      'activity': serializers.ChoiceField(required=True, choices=['like', 'edit']),
      'article': serializers.IntegerField(required=True),
      'user': serializers.IntegerField(required=True)
    }, data=args)
    if validator.is_valid():
      args = validator.validated_data
      can_create = True
      
      if activity == 'like':
        can_create = not ActivityLogQueries().get_activities(args).count()

      if can_create:
        ActivityLogCommands().create_activity_log(args)
    
    return redirect('articles')
