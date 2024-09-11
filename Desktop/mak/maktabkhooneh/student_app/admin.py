from django.contrib.admin import register, ModelAdmin
from teacher_app.models import Teacher


@register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = [
                    'name',
                    'email',
    ]
    search_fields = ['name',
    ]