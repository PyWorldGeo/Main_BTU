# Generated by Django 3.2.1 on 2024-06-19 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='book',
            new_name='books',
        ),
    ]
