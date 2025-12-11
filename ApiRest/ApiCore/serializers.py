"""Serializers for ApiCore models.

Each serializer maps a model to JSON input/output used by the API.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Company, Equipment, Technician, MaintenancePlan, WorkOrder


class CompanySerializer(serializers.ModelSerializer):
    """Serializer para `Company`.

    Devuelve campos básicos y es utilizado por el viewset de compañías.
    """
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'rut', 'created_at']


class EquipmentSerializer(serializers.ModelSerializer):
    """Serializer para `Equipment`.

    `company` se representa como clave primaria (ID) en la API.
    """
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Equipment
        fields = ['id', 'company', 'name', 'serial_number', 'critical', 'installed_at']


class TechnicianSerializer(serializers.ModelSerializer):
    """Serializer para `Technician`.

    El campo `user` referencia al `AUTH_USER_MODEL` por su ID.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Technician
        fields = ['id', 'user', 'full_name', 'specialty', 'phone']


class MaintenancePlanSerializer(serializers.ModelSerializer):
    """Serializer para `MaintenancePlan`.

    `equipment` se pasa por su ID.
    """
    equipment = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())

    class Meta:
        model = MaintenancePlan
        fields = ['id', 'equipment', 'name', 'frequency_days', 'active']


class WorkOrderSerializer(serializers.ModelSerializer):
    """Serializer para `WorkOrder`.

    Incluye referencias a `plan`, `equipment` y `technician` por ID.
    """
    plan = serializers.PrimaryKeyRelatedField(queryset=MaintenancePlan.objects.all(), allow_null=True, required=False)
    equipment = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    technician = serializers.PrimaryKeyRelatedField(queryset=Technician.objects.all(), allow_null=True, required=False)

    class Meta:
        model = WorkOrder
        fields = ['id', 'plan', 'equipment', 'technician', 'status', 'scheduled_date', 'completed_at', 'notes']
