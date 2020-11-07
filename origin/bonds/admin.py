from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Bond


class BondAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    fieldsets = (
        (_('Details'), {'fields': ('lei', 'legal_name', 'isin', 'size', 'currency', 'maturity')}),
    )
    readonly_fields = ('legal_name',)
    list_filter = ('legal_name',)
    list_display = ('lei', 'legal_name', 'isin', 'size', 'currency', 'maturity',)


admin.site.register(Bond, BondAdmin)
