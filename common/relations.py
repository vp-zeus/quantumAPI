from rest_framework import serializers


class SerializablePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def __init__(self, **kwargs):
        self.FieldSerializer = kwargs.pop('field_serializer')
        super().__init__(**kwargs)

    def to_representation(self, value):
        result = super().to_representation(value)
        model_instance = self.get_queryset().get(pk=result)
        return self.FieldSerializer(model_instance).data
