from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'equipments', views.EquipmentViewSet)
router.register(r'technicians', views.TechnicianViewSet)
router.register(r'maintenance-plans', views.MaintenancePlanViewSet)
router.register(r'work-orders', views.WorkOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ping/', views.ping, name='api-ping'),
]
