# Generated by Django 4.2.2 on 2023-06-13 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0002_about_meditation_page_meditation_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meditation',
            old_name='med_Fname',
            new_name='genre',
        ),
    ]
