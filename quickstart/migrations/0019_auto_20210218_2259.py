# Generated by Django 3.1.3 on 2021-02-19 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0018_testclassword'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneratorBlobs',
            new_name='Blobs',
        ),
        migrations.DeleteModel(
            name='TestClassWord',
        ),
    ]
