from rest_framework import serializers

from . import models


class SubmissionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Submission
        fields = [
            'status',
            'runid',
            'timeused',
            'memoryused',
            'errorinfo',
            'submit_datetime',
            'judge_datetime'
        ]


class SubmissionSerializer(serializers.Serializer):
    soj = serializers.CharField(label='OJ名称', max_length=128)
    sid = serializers.IntegerField(label='题目编号')
    code = serializers.CharField(label='代码', min_length=50)
    lang = serializers.CharField(label='语言名称', max_length=128)
