from rest_framework import serializers

from . import models


class OJSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OJ
        fields = '__all__'
