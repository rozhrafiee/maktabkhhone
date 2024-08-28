from django.contrib.admin import register, ModelAdmin
from cupon_app.models import Cupon

@register(Cupon)
class CuponAdmin(ModelAdmin):
    pass