from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.custom_openapi import surname, department_id
from employer.models import Employer
from employer.paginations import ListPagination
from employer.serializers import EmployerSerializer


class EmployerListAPIView(generics.ListAPIView):
    """
        Api view for get all employer list
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    pagination_class = ListPagination

    def get_queryset(self):
        query_surname = self.request.query_params.get('surname')
        query_department_id = self.request.query_params.get('department_id')

        filters = []

        if query_surname:
            filters.append(Q(surname__icontains=query_surname))
        if query_department_id:
            filters.append(Q(department_id=query_department_id))

        return Employer.objects.filter(*filters)

    @swagger_auto_schema(manual_parameters=[surname, department_id])
    def get(self, request, *args, **kwargs):
        return super(EmployerListAPIView, self).get(request, *args, **kwargs)


class EmployerDepListAPIView(generics.ListAPIView):
    """
        Api view for get all employer list by department
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployerSerializer

    def get_queryset(self):
        return Employer.objects.filter(department_id=self.kwargs.get('department_id'))


class EmployerCreateAPIView(generics.GenericAPIView):
    """
        Api view for get adding employer
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerDeleteAPIView(generics.DestroyAPIView):
    """
        Api view for get deleting employer
    """
    permission_classes = (IsAuthenticated,)
    queryset = Employer.objects.all()
    lookup_field = 'id'
