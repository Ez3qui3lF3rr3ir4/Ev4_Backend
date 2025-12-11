"""Viewsets y endpoints de ApiCore.

Se exponen ModelViewSet para cada entidad para proporcionar CRUD RESTful
con control de permisos centralizado en `settings.py`.
"""

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Company, Equipment, Technician, MaintenancePlan, WorkOrder
from .serializers import (
	CompanySerializer,
	EquipmentSerializer,
	TechnicianSerializer,
	MaintenancePlanSerializer,
	WorkOrderSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
	"""CRUD completo para `Company`.

	Permisos por defecto: `IsAuthenticatedOrReadOnly` (definido en settings).
	"""
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class EquipmentViewSet(viewsets.ModelViewSet):
	"""CRUD para `Equipment`."""
	queryset = Equipment.objects.all()
	serializer_class = EquipmentSerializer


class TechnicianViewSet(viewsets.ModelViewSet):
	"""CRUD para `Technician` (perfiles de técnicos)."""
	queryset = Technician.objects.all()
	serializer_class = TechnicianSerializer


class MaintenancePlanViewSet(viewsets.ModelViewSet):
	"""CRUD para `MaintenancePlan`."""
	queryset = MaintenancePlan.objects.all()
	serializer_class = MaintenancePlanSerializer


class WorkOrderViewSet(viewsets.ModelViewSet):
	"""CRUD para `WorkOrder` (órdenes de trabajo)."""
	queryset = WorkOrder.objects.all()
	serializer_class = WorkOrderSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def ping(request):
	"""Endpoint de prueba para verificar que la API responde."""
	return Response({'status': 'ok', 'message': 'API is working'})
