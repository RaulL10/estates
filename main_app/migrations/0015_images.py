# Generated by Django 2.2.12 on 2022-04-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20220418_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('profile', models.FileField(upload_to='files')),
            ],
        ),
    ]
