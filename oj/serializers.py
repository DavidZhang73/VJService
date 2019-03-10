from rest_framework import serializers

from . import models


class OJLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = [
            'id',
            'name',
            'code'
        ]


class OJSerializer(serializers.ModelSerializer):
    language = OJLanguageSerializer(required=False, many=True)

    class Meta:
        model = models.OJ
        fields = [
            'id',
            'name',
            'start_sid',
            'end_sid',
            'language',
        ]


class OJListSerializer(serializers.ModelSerializer):
    url = serializers.URLField()

    class Meta:
        model = models.OJ
        fields = [
            'id',
            'url',
            'name'
        ]
