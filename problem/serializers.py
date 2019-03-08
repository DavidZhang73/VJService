from rest_framework import serializers

from . import models


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = '__all__'


class ProblemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = [
            'id',
            'soj',
            'sid',
            'title',
            'source'
        ]
