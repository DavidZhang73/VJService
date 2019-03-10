from django.urls import path

from . import views

urlpatterns = [
    path('', views.OJListAPIView.as_view()),
    path('<str:soj>/', views.OJAPIView.as_view()),
]
