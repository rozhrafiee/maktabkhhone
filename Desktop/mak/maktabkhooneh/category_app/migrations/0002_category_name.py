# Generated by Django 5.1 on 2024-08-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
