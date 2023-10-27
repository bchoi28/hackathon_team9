from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'restaurant_employee_id', 'roles', 'food_permit_exp',
                  'alcohol_permit_exp', 'is_former_employee', 'created_at', 'updated_at', 'sheet_cell', 'is_uploaded']
        depth = 1


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role', 'description', 'employees', 'created_at',
                  'updated_at', 'sheet_cell', 'is_uploaded']
        depth = 1
