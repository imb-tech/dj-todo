from rest_framework import serializers

from . import models



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'position',
            'age',
            'phone'
        )
