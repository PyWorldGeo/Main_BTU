# Generated by Django 3.2.1 on 2024-06-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.TextField(max_length=1000),
        ),
    ]
