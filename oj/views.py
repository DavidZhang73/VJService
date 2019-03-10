from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class OJListAPIView(APIView):
    def get(self, request):
        oj_list = models.OJ.objects.all()
        data = []
        for oj in oj_list:
            oj.url = f'{request.get_raw_uri()}{oj.name}'
            d = serializers.OJListSerializer(oj).data
            data.append(d)
        return Response({
            'count': len(data),
            'results': data
        })


class OJAPIView(APIView):
    def get(self, request, soj):
        oj = get_object_or_404(models.OJ, name=soj)
        language = models.Language.objects.filter(oj__name=soj)
        oj.language = language
        data = serializers.OJSerializer(oj).data
        return Response(data)
