from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Gender(models.Model):
    short_name = models.CharField(max_length=5, )
    long_name = models.CharField(max_length=100, )
    is_active = models.BooleanField(default=True, )

    def __str__(self):
        return self.long_name


class BasePlace(models.Model):
    name = models.CharField(
        _('name'),
        max_length=250
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{0}".format(self.name)


class Country(BasePlace):
    alpha2code = models.CharField(
        _('code two letters'),
        max_length=2,
        unique=True
    )
    alpha3code = models.CharField(
        _('code three letters'),
        max_length=3,
        unique=True
    )
    numeric_code = models.IntegerField(
        _('code numeric'),
        unique=True
    )
    phone_prefix = models.IntegerField(
        _('prefix numeric'),
        # unique=True,
        default=0
    )
    is_active = models.BooleanField(default=True, )
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Language(BasePlace):
    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    code = models.CharField(
        _("code"),
        max_length=2,
    )
    is_active = models.BooleanField(default=True, )
