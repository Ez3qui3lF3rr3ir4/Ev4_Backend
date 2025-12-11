from django.contrib import admin
from .models import Company, Equipment, Technician, MaintenancePlan, WorkOrder


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'rut', 'created_at')
	search_fields = ('name', 'rut')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'serial_number', 'company', 'critical', 'installed_at')
	list_filter = ('company', 'critical')
	search_fields = ('name', 'serial_number')


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
	list_display = ('id', 'full_name', 'user', 'specialty', 'phone')
	search_fields = ('full_name', 'specialty', 'phone')


@admin.register(MaintenancePlan)
class MaintenancePlanAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'equipment', 'frequency_days', 'active')
	list_filter = ('active',)
	search_fields = ('name',)


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'plan', 'equipment', 'technician', 'status', 'scheduled_date', 'completed_at')
	list_filter = ('status',)
	search_fields = ('plan__name', 'equipment__name')
