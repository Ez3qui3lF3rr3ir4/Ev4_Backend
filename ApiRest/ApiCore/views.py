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
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class EquipmentViewSet(viewsets.ModelViewSet):
	queryset = Equipment.objects.all()
	serializer_class = EquipmentSerializer


class TechnicianViewSet(viewsets.ModelViewSet):
	queryset = Technician.objects.all()
	serializer_class = TechnicianSerializer


class MaintenancePlanViewSet(viewsets.ModelViewSet):
	queryset = MaintenancePlan.objects.all()
	serializer_class = MaintenancePlanSerializer


class WorkOrderViewSet(viewsets.ModelViewSet):
	queryset = WorkOrder.objects.all()
	serializer_class = WorkOrderSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def ping(request):
	"""Endpoint de prueba para verificar que la API responde."""
	return Response({'status': 'ok', 'message': 'API is working'})
