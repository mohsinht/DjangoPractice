from rest_framework import serializers
from status.models import Status

'''
A serializer does 2 basic things:
1. Serializers -> JSON
2. Serializers -> Validate Data
'''


# Serializers turn Models or Query Sets into Native Python data that can be converted into JSON/(or parseable) format
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    # validata_<field_name>()
    def validate_content(self, value):
        if len(value) > 10000:
            raise serializers.ValidationError('Too long content')
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if image is None and content is None:
            raise serializers.ValidationError('Content or image is required')

        return data
