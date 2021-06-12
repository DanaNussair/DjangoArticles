from django.shortcuts import render, redirect
from rest_framework import serializers

# Services
from .services.commands import CategoryCommands
from .services.common import CommonCategoryServices
# Support
from support.validator import Validator


class CategoryViews():
  def create(request):
    is_authenticated = request.user.is_authenticated
    message = None

    if is_authenticated and request.POST:
      validator = Validator().validate(fields={
        'title': serializers.CharField(required=True, trim_whitespace=True),
        'description': serializers.CharField(required=False, trim_whitespace=True)
      }, data=request.POST)
      if validator.is_valid():
        args = validator.validated_data
      
        created = CategoryCommands().create_category(args)
        if 'data' in created:
          return redirect('articles_create')
        else:
          message = "Can not create category"
      else:
          message = "Invalid parameters"

    return render(request, 'categories/create_category.html', 
      {'title': 'Create Category', 'message': message})
