from rest_framework import serializers

from department.models import Department
from employer.models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'name', 'surname', 'avatar', 'position', 'salary', 'age', 'department')
