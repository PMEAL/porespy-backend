# Generated by Django 3.1.3 on 2021-03-15 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0022_localthickness_generator_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localthickness',
            old_name='generator_image',
            new_name='local_thickness_image',
        ),
    ]
