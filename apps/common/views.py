from rest_framework import viewsets
from . import serializers, models


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()
    permission_classes = ()
    authentication_classes = ()
