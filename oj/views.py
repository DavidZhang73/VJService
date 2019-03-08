from rest_framework import viewsets

from . import models, serializers


class OJViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.OJSerializer
    queryset = models.OJ.objects.all()
