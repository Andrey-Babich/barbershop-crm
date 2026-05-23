from rest_framework.routers import DefaultRouter

from .views import (
    MasterViewSet,
    ServiceViewSet,
    AppointmentViewSet
)

router = DefaultRouter()

router.register(r'masters', MasterViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls