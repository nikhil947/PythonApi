from rest_framework import serializers
from . models import employees

class employeeSerializers(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields='__all__'

