# Generated by Django 4.0.2 on 2022-04-19 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_alter_realtor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='image',
        ),
    ]
