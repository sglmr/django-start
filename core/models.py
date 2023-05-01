from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating 'created' and 'modified' fields.
    """

    created = models.DateTimeField(auto_now_add=True, help_text="Date time object was created.")
    modified = models.DateTimeField(auto_now=True, help_text="Date time object was last modified.")

    class Meta:
        abstract = True
