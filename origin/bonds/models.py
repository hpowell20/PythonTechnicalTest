from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import models

from .utils import get_lei_legal_name


class Bond(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    lei = models.CharField(max_length=20, null=False)
    legal_name = models.TextField(blank=True, null=True, default=None)
    isin = models.CharField(max_length=20, null=False)
    size = models.IntegerField(default=0)
    currency = models.CharField(max_length=5, null=False)
    maturity = models.DateField(null=False)

    created_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        try:
            self.legal_name = get_lei_legal_name(self.lei)
        except Exception as e:
            raise ValidationError({'lei': [e]})

    class Meta:
        unique_together = ('lei', 'user',)
        ordering = ('lei', 'created_date',)
        db_table = 'bond'

    def __str__(self):
        return self.lei
