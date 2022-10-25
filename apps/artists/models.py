from django.db import models
from django.utils.translation import gettext_lazy as _
from core import settings


# Create your models here.

class Artist(models.Model):
    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.RESTRICT,
    )
    link = models.URLField(
        max_length=350,
        help_text=_('The url of the artist'),
        blank=True,
    )
    share = models.URLField(
        max_length=350,
        help_text=_('The share link of the artist'),
        blank=True,
    )
    picture = models.ImageField(
        help_text=_("The url of the artist picture."),
        upload_to="images/artist/",
        default='images/artist/avatar-default.png',
    )
    nb_album = models.IntegerField(
        help_text=_("The number of artist's albums"),
        null=True,
    )
    nb_fan = models.IntegerField(
        help_text=_("The number of artist's fans"),
        null=True,
    )
    radio = models.BooleanField(
        default=False, verbose_name=_("radio"),
        help_text=_('true if the artist has a smartradio'),
    )
    tracklist = models.URLField(
        max_length=350,
        help_text=_('API Link to the top of this artist'),
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("is active"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def name(self):
        return f'{format(self.user.first_name)}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
