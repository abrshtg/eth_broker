from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("Broker", "Broker"),
        ("Client", "Client"),
    )
    role = models.CharField(
        max_length=6, choices=ROLE_CHOICES, default="Client")
    name = models.CharField(max_length=100)


class Broker(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="broker_profile"
    )
    services_offered = models.TextField(max_length=500)


class Property(models.Model):
    broker = models.ForeignKey(
        Broker, on_delete=models.CASCADE, related_name="property_listing"
    )
    property_name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=100)


class Enquiry(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="client_enquiries",
        limit_choices_to={"role": "Client"},
    )
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="property_enquiries"
    )
    enquiry_message = models.TextField(max_length=500)
    enquiry_date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_feedback"
    )
    broker = models.ForeignKey(
        Broker, on_delete=models.CASCADE, related_name="broker_feedback"
    )
    feedback = models.TextField(max_length=500)
    rating = models.PositiveSmallIntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
