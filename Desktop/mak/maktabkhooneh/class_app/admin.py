from django.contrib.admin import register , ModelAdmin
from class_app.models import Clas

@register(Clas)
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
    