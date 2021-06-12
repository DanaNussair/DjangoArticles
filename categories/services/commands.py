from categories.models import Category
from categories.serializers import CategorySerializer

class CategoryCommands():
  def create_category(self, args={}):
    try:
      serializer = CategorySerializer(data=args)
      if serializer.is_valid():
        serializer.save()
        return {'data': serializer.data}
      else:
        return {'error': 'Provided parameters are incorrect'}
    except Exception as err:
      print('Error occurred in create_category', err)
      return {'error': 'Could not create category'}

