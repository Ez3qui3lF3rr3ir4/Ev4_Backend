"""
Core models for the maintenance API.

Includes models for Company, Equipment, Technician, MaintenancePlan and WorkOrder.
"""

from django.conf import settings
from django.db import models


class Company(models.Model):
	"""Empresa — representa una compañía cliente.

	Fields:
	- name: nombre de la empresa
	- address: dirección física
	- rut: identificador fiscal (único)
	- created_at: marca de tiempo de creación
	"""
	name = models.CharField(max_length=255)
	address = models.TextField(blank=True)
	rut = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Equipment(models.Model):
	"""Equipo — equipo físico perteneciente a una `Company`.

	Fields:
	- company: FK a Company
	- name: nombre descriptivo
	- serial_number: número de serie único
	- critical: flag que indica criticidad
	- installed_at: fecha de instalación
	"""
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='equipments')
	name = models.CharField(max_length=255)
	serial_number = models.CharField(max_length=255, unique=True)
	critical = models.BooleanField(default=False)
	installed_at = models.DateField(null=True, blank=True)

	def __str__(self):
		return f"{self.name} ({self.serial_number})"


class Technician(models.Model):
	"""Técnico — perfil asociado a un usuario de Django.

	La relación OneToOne con `AUTH_USER_MODEL` permite distinguir técnicos
	y asignarles órdenes de trabajo.
	"""
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='technician_profile')
	full_name = models.CharField(max_length=255)
	specialty = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.full_name


class MaintenancePlan(models.Model):
	"""Plan de Mantención — define frecuencia y si está activo.

	Fields:
	- equipment: FK al equipo al que aplica
	- name: nombre del plan
	- frequency_days: intervalo en días
	- active: activo/inactivo
	"""
	equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_plans')
	name = models.CharField(max_length=255)
	frequency_days = models.PositiveIntegerField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.name} - {self.equipment}"


class WorkOrder(models.Model):
	"""Orden de Trabajo — instancia de trabajo creada a partir de un plan.

	Status choices:
	- pending, scheduled, in_progress, completed, cancelled
	"""
	STATUS_PENDING = 'pending'
	STATUS_SCHEDULED = 'scheduled'
	STATUS_IN_PROGRESS = 'in_progress'
	STATUS_COMPLETED = 'completed'
	STATUS_CANCELLED = 'cancelled'

	STATUS_CHOICES = [
		(STATUS_PENDING, 'Pending'),
		(STATUS_SCHEDULED, 'Scheduled'),
		(STATUS_IN_PROGRESS, 'In Progress'),
		(STATUS_COMPLETED, 'Completed'),
		(STATUS_CANCELLED, 'Cancelled'),
	]

	plan = models.ForeignKey(MaintenancePlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='work_orders')
	equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='work_orders')
	technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True, blank=True, related_name='work_orders')
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
	scheduled_date = models.DateTimeField(null=True, blank=True)
	completed_at = models.DateTimeField(null=True, blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return f"WorkOrder #{self.pk} - {self.equipment} - {self.status}"

