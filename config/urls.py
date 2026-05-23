from django.contrib import admin

from django.urls import path
from django.urls import include

from graphene_django.views import GraphQLView

from salon.views import (
    home,
    booking_page,
    create_appointment
)


urlpatterns = [

    path('', home),

    path(
        'booking/<int:master_id>/',
        booking_page
    ),

    path(
        'create-appointment/',
        create_appointment
    ),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/',
        include('salon.urls')
    ),

    path(
        'graphql/',
        GraphQLView.as_view(graphiql=True)
    ),
]