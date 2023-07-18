from rest_framework import serializers

from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    employer_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'employer_count', 'total_salary')

    def get_employer_count(self, obj):
        return (
            obj.employer_count if hasattr(obj, 'employer_count') else 0
        )

    def get_total_salary(self, obj):
        return (
            obj.total_salary if hasattr(obj, 'total_salary') else 0
        )
