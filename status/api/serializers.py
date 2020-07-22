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
