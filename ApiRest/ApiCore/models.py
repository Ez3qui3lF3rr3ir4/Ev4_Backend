from django.conf import settings
from django.db import models


class Company(models.Model):
	"""Empresa"""
	name = models.CharField(max_length=255)
	address = models.TextField(blank=True)
	rut = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Equipment(models.Model):
	"""Equipo"""
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='equipments')
	name = models.CharField(max_length=255)
	serial_number = models.CharField(max_length=255, unique=True)
	critical = models.BooleanField(default=False)
	installed_at = models.DateField(null=True, blank=True)

	def __str__(self):
		return f"{self.name} ({self.serial_number})"


class Technician(models.Model):
	"""Técnico"""
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='technician_profile')
	full_name = models.CharField(max_length=255)
	specialty = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.full_name


class MaintenancePlan(models.Model):
	"""Plan de Mantención"""
	equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_plans')
	name = models.CharField(max_length=255)
	frequency_days = models.PositiveIntegerField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.name} - {self.equipment}"


class WorkOrder(models.Model):
	"""Orden de Trabajo"""
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

