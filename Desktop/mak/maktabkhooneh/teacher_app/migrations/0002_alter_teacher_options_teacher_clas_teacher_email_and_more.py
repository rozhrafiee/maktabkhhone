# Generated by Django 5.1 on 2024-08-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0002_clas_delete_class'),
        ('teacher_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='clas',
            field=models.ManyToManyField(help_text='Enter the class of the teacher.', related_name='teacher', to='class_app.clas', verbose_name='Class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='', help_text='Enter the Email of the teacher.', max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(default='', help_text='Enter the first name of the teacher.', max_length=50, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default='', help_text='Enter the last name of the teacher.', max_length=50, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default='', help_text='Enter the phone number of the teacher.', max_length=11, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='rate',
            field=models.FloatField(default=0, help_text='Enter the rate of the teacher.', verbose_name='Rate'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='wallet',
            field=models.FloatField(default=0, help_text="Enter the current balance in the teacher's wallet.", verbose_name='Wallet Balance'),
        ),
    ]
