from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    MasterViewSet,
    ServiceViewSet,
    AppointmentViewSet,
    booking,
    create_appointment,
    register,
    index
)

router = DefaultRouter()

router.register(r'masters', MasterViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [

    # Главная страница
    path('', register),

    # Регистрация
    path(
        'register/',
        register,
        name='register'
    ),

    # Django login/logout
    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),

    # Главная страница после входа
    path(
        'home/',
        index,
        name='home'
    ),

    # Страница записи
    path(
        'booking/<int:master_id>/',
        booking,
        name='booking'
    ),

    # Создание записи
    path(
        'create-appointment/',
        create_appointment,
        name='create_appointment'
    ),

]

urlpatterns += router.urls