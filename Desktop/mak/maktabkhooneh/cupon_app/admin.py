from django.contrib.admin import register, ModelAdmin
from cupon_app.models import Cupon

@register(Cupon)
class CuponAdmin(ModelAdmin):
    list_display = [
        'title',
        'expire_date',
        'percent',
        'cupon_availability'
    ]
    search_fields = [
        'title'
    ]