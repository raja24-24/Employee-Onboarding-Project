from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Devdetails
from .models import EmployeeInfo
from .models import Employee
from .models import Developer


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devdetails
        fields = '__all__'



class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'


class DeveloperDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devdetails
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'password']

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['employee_id', 'password']