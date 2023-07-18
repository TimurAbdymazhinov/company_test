from django.db.models import Count, Sum
from rest_framework import generics
from rest_framework.permissions import AllowAny

from department.models import Department
from department.serializers import DepartmentSerializer


class DepartmentListAPIView(generics.ListAPIView):
    """
        Api view for get all department list
    """
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return (
            Department.objects.all()
                .prefetch_related('employers')
                .annotate(
                    employer_count=Count('employers'),
                    total_salary=Sum('employers__salary')
                )
        )
