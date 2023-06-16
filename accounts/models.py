from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """A custom user model for the project."""

    first_name = None
    last_name = None
    name = models.CharField(_("name"), max_length=150, blank=True)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name.strip()
