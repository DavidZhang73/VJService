from django.urls import path

from . import views

urlpatterns = [
    path('', views.SubmissionAPIView.as_view()),
    path('<uuid:uuid>/', views.SubmissionStatusAPIView.as_view())
]
