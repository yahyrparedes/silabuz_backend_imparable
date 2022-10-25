from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.commons.models import Gender, Country, Language
from core import settings


# Create your models here.
class Client(models.Model):
    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.RESTRICT)

    date_of_birth = models.DateField(
        _("date of birth"),
        blank=True,
        null=True,
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_("The user's gender")
    )
    link = models.URLField(
        max_length=350,
        blank=True,
        verbose_name=_("link"),
        help_text=_("The url of the profile for the user")
    )
    picture = models.ImageField(
        _("picture"),
        upload_to="images/client/",
        default='images/client/avatar-default.jpeg',
        help_text=_("The url of the user's profil picture")
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_("The user's country")
    )
    lang = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_("The user's lang")
    )
    is_kid = models.BooleanField(_("is kid"), default=False, )
    tracklist = models.URLField(
        max_length=350,
        help_text=_("API Link to the flow of this user"),
        blank=True,
    )
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def lastname(self):
        return f'{self.user.last_name}'

    def firstname(self):
        return f'{self.user.first_name}'

    def _gender(self):
        return self.gender.short_name if self.gender is not None else '-'

    def _country(self):
        return self.country.name if self.country is not None else '-'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
