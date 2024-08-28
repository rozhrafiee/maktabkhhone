from django.contrib.admin import register, ModelAdmin
from cupon_app.models import Cupon

@register(Cupon)
class CuponAdmin(ModelAdmin):
    list_display = [
        'code',
        'discount',
        'expiry_date',
    ]
    search_fields = [
        'code',
        'discount',
        'expiry_date',
    ]