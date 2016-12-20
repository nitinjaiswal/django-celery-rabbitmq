from django.db import models


class UserDetail(models.Model):
    """
    Model for storing user name, mobile number and email id
    """
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=100)


class UserAddress(models.Model):
    """
    Model for storing user address
    """
    address = models.CharField(max_length=200)
