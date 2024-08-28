from django.contrib.admin import register , ModelAdmin
from factor_app.models import Factor

@register(Factor)
class FactorAdmin(ModelAdmin):
    list_display = [
        'student_name',
        'price',
        'cupon',
        # 'class1',
        'payment_status',
    ]
    search_fields = [
        'name',
    ]
    