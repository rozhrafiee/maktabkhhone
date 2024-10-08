# Generated by Django 5.1 on 2024-08-28 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0002_category_name'),
        ('class_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_app.category')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
