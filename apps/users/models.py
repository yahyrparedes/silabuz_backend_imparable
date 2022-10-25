from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

from apps.users.managers import UserManager


# Create your models here.
class User(AbstractUser):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(max_length=150, blank=True, )
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _('email address'),
        help_text=_('Please insert your email'),
        max_length=255,
        unique=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        index_together = ['email']

    def __str__(self):
        return '{0}'.format(self.email)
