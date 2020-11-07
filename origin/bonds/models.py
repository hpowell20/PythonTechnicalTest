from django.core.exceptions import ValidationError
from django.db import models

from .utils import get_lei_legal_name


class Bond(models.Model):
    lei = models.CharField(max_length=100, unique=True, null=False)
    legal_name = models.TextField(blank=True, null=True, default=None)
    isin = models.CharField(max_length=100, null=False)
    size = models.IntegerField(default=0)
    currency = models.CharField(max_length=50, null=False)
    maturity = models.DateField(null=False)

    created_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        try:
            self.legal_name = get_lei_legal_name(self.lei)
        except Exception as e:
            raise ValidationError({'lei': [e]})

    class Meta:
        ordering = ('created_date',)
        db_table = 'bond'

    def __str__(self):
        return self.lei
