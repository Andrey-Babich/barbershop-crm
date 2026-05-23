from django.db import models


class Master(models.Model):

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    position = models.CharField(
        max_length=100
    )

    photo = models.ImageField(
        upload_to='barbers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return (
            f"{self.first_name} "
            f"{self.last_name}"
        )


class Service(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):

    client_name = models.CharField(max_length=100)

    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.CharField(
        max_length=10
    )

    def __str__(self):
        return (
            f"{self.client_name} - "
            f"{self.master.first_name}"
        )