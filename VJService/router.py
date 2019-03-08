from rest_framework.routers import DefaultRouter

from oj.views import OJViewSet
from problem.views import ProblemViewSet

router = DefaultRouter()
router.register(r'problem', ProblemViewSet, basename='problem')
router.register(r'oj', OJViewSet, basename='oj')
