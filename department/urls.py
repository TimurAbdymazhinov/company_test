from django.urls import path

from department.views import DepartmentListAPIView

urlpatterns = [
    path('', DepartmentListAPIView.as_view(), name='departments-list')
]
