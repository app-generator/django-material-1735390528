# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    userid = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    employeeid = models.ForeignKey(Employee, on_delete=models.CASCADE)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Employee(models.Model):

    #__Employee_FIELDS__
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    phone1 = models.IntegerField(null=True, blank=True)
    phone2 = models.IntegerField(null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Country(models.Model):

    #__Country_FIELDS__
    countryid = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    #__Country_FIELDS__END

    class Meta:
        verbose_name        = _("Country")
        verbose_name_plural = _("Country")


class City(models.Model):

    #__City_FIELDS__
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)

    #__City_FIELDS__END

    class Meta:
        verbose_name        = _("City")
        verbose_name_plural = _("City")



#__MODELS__END
