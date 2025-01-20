from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    start_date = models.DateTimeField(
        _('Start Date'),
        help_text=_('The start date and time of the travel'),
        null=True,
        blank=True,
    )
    end_date = models.DateTimeField(
        _('End Date'),
        help_text=_('The end date and time of the travel'),
        null=True,
        blank=True,
    )
    is_approved = models.BooleanField(
        _('Approved'),
        default=False,
        help_text=_('Indicates if the travel product has been approved by admin')
    )
    vendor = models.ForeignKey('partner.Partner', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('Travel Product')
        verbose_name_plural = _('Travel Products')

    def clean(self):
        super().clean()
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError({
                'end_date': _('End date must be after start date.')
            })

from oscar.apps.catalogue.models import *  # noqa isort:skip
