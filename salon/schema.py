import graphene

from graphene_django import DjangoObjectType

from .models import Master, Service, Appointment


class MasterType(DjangoObjectType):
    class Meta:
        model = Master
        fields = "__all__"


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        fields = "__all__"


class AppointmentType(DjangoObjectType):
    class Meta:
        model = Appointment
        fields = "__all__"


class Query(graphene.ObjectType):
    all_masters = graphene.List(MasterType)

    all_services = graphene.List(ServiceType)

    all_appointments = graphene.List(AppointmentType)

    def resolve_all_masters(root, info):
        return Master.objects.all()

    def resolve_all_services(root, info):
        return Service.objects.all()

    def resolve_all_appointments(root, info):
        return Appointment.objects.all()


schema = graphene.Schema(query=Query)
