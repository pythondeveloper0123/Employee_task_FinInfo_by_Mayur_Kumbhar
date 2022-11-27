from django.urls import path
from .views import EmployeeGetPostAPIView, EmployeeGetPutDeleteAPIView

urlpatterns = [
    path('emp/', EmployeeGetPostAPIView.as_view()),
    path('emp/<int:pk>/', EmployeeGetPutDeleteAPIView.as_view()),
]
