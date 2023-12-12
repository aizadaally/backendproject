from rest_framework import serializers
from . import models
from api import models


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
        fields = ('__all__')

class RecordDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
        fields = ('__all__')    
        

class StaffSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.Staff
        fields = ('__all__')

class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = ('__all__')
        

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('__all__')

class DepartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('__all__')



