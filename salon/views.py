from django.shortcuts import render

from django.http import JsonResponse

from rest_framework import viewsets

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, date

from .models import (
    Master,
    Service,
    Appointment
)

from .serializers import (
    MasterSerializer,
    ServiceSerializer,
    AppointmentSerializer
)


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def home(request):

    masters = Master.objects.all()

    return render(
        request,
        'index.html',
        {
            'masters': masters
        }
    )


def booking_page(request, master_id):

    master = Master.objects.get(id=master_id)

    services = Service.objects.all()

    selected_date = request.GET.get("date")

    if not selected_date:
        selected_date = str(date.today())

    appointments = Appointment.objects.filter(
        master=master,
        appointment_date=selected_date
    )

    booked_times = []

    for appointment in appointments:
        booked_times.append(
            appointment.appointment_time
        )

    time_slots = [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
    ]

    return render(
        request,
        'booking.html',
        {
            'master': master,
            'services': services,
            'time_slots': time_slots,
            'booked_times': booked_times,
            'selected_date': selected_date
        }
    )


@csrf_exempt
def create_appointment(request):

    if request.method == "POST":

        client_name = request.POST.get(
            "client_name"
        )

        master_id = request.POST.get(
            "master_id"
        )

        service_id = request.POST.get(
            "service_id"
        )

        selected_date = request.POST.get(
            "date"
        )

        selected_time = request.POST.get(
            "time"
        )

        if (
            not client_name
            or not service_id
            or not selected_date
            or not selected_time
        ):

            return JsonResponse({
                "success": False,
                "message": "Fill all fields"
            })

        if any(char.isdigit() for char in client_name):

            return JsonResponse({
                "success": False,
                "message":
                    "Name cannot contain numbers"
            })

        today = date.today()

        booking_date = datetime.strptime(
            selected_date,
            "%Y-%m-%d"
        ).date()

        if booking_date < today:

            return JsonResponse({
                "success": False,
                "message":
                    "Date cannot be in the past"
            })

        if (
            booking_date.year >
            today.year + 1
        ):

            return JsonResponse({
                "success": False,
                "message":
                    "Date is too far"
            })

        existing = Appointment.objects.filter(
            master_id=master_id,
            appointment_date=selected_date,
            appointment_time=selected_time
        ).exists()

        if existing:

            return JsonResponse({
                "success": False,
                "message":
                    "This time is already booked"
            })

        Appointment.objects.create(

            client_name=client_name,

            master=Master.objects.get(
                id=master_id
            ),

            service=Service.objects.get(
                id=service_id
            ),

            appointment_date=selected_date,

            appointment_time=selected_time
        )

        return JsonResponse({
            "success": True,
            "message":
                "Appointment booked!"
        })

    return JsonResponse({
        "success": False
    })