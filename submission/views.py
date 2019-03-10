from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers, tasks


class SubmissionStatusAPIView(APIView):
    def get(self, request, uuid):
        submission = get_object_or_404(models.Submission, id=uuid)
        data = serializers.SubmissionStatusSerializer(submission).data
        return Response(data)


class SubmissionAPIView(APIView):
    def post(self, request):
        data = serializers.SubmissionSerializer(request.data).data
        submission = models.Submission.objects.create(
            problem=get_object_or_404(models.Problem, soj=data.get('soj'), sid=data.get('sid')),
            code=data.get('code'),
            lang=get_object_or_404(models.Language, name=data.get('lang')),
        )
        tasks.submit.delay(
            soj=submission.problem.soj,
            sid=submission.problem.sid,
            code=submission.code,
            lang=submission.lang.name,
            id=submission.id
        )
        return Response({
            'id': submission.id,
            'url': f'{request.get_raw_uri()}{submission.id}'
        })
