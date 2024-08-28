from django.contrib.admin import register, ModelAdmin
from teacher_app.models import Teacher
@register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'clas',
        'category',
        'rate',
        'wallet',
    ]
    search_fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'clas',
        'category',
        'rate',
    ]