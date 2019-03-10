from rest_framework.routers import DefaultRouter

from problem.views import ProblemViewSet

router = DefaultRouter()
router.register(r'problem', ProblemViewSet, basename='problem')
# router.register(r'oj', OJViewSet, basename='oj')
# router.register(r'submission', SubmissionViewSet, basename='submission')
