from rest_framework import serializers

class Validator():
  @staticmethod
  def create_serializer(name, fields):
    return type(name, (serializers.Serializer,), fields)

  @staticmethod
  def validate(*, fields, data=None, **kwargs):
    serializer_class = Validator.create_serializer(
      name='', fields=fields
    )

    if data:
      return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)