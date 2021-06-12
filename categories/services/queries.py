from categories.models import Category
from categories.serializers import CategorySerializer

class CategoryQueries():
  def get_category_queryset(self, filters={}):
    try:
      category = Category.objects.get(**filters)
      return category
    except Exception as err:
      print('Error occurred in get_category_queryset: ', err)
      return Category.objects.none()

  def get_categories_queryset(self, filters={}, order_by=[]):
    try:
      categories = Category.objects.filter(**filters).order_by(*order_by)
      return categories
    except Exception as err:
      print('Error occurred in get_categories_queryset: ', err)
      return Category.objects.none()