# Generated by Django 3.2.4 on 2021-07-20 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackxsps', '0003_auto_20210718_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='domain',
            new_name='track',
        ),
    ]