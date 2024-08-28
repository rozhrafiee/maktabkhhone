from django.contrib.admin import register, ModelAdmin
from teacher_app.models import Teacher

@register(Teacher)
class TeacherAdmin(ModelAdmin):
    pass
