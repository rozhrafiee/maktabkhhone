from django.contrib.admin import register , ModelAdmin
from class_app.models import Class

@register(Class)
class ClassAdmin(ModelAdmin):
    list_display = [
        'name',
        'price',
        'time',
        'time',
        'category',
    ]
    search_fields = [
        'name',
    ]
    