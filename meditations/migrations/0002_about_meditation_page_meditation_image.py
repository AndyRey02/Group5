# Generated by Django 4.2.2 on 2023-06-13 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('about_page_ID', models.AutoField(primary_key=True, serialize=False)),
                ('creator_ID', models.DateField(auto_now_add=True)),
                ('user_ID', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='meditation_page',
            name='meditation_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
