from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ProblemInfoSerializer
    queryset = models.Problem.objects.all()
    filterset_fields = ('soj', 'source')
    search_fields = ('soj', 'sid', 'title', 'source')
    ordering_fields = ('soj', 'sid')


class ProblemAPIView(APIView):
    def get(self, request, soj, sid):
        p = get_object_or_404(models.Problem, soj=soj, sid=sid)
        data = serializers.ProblemSerializer(p).data
        return Response(data)
