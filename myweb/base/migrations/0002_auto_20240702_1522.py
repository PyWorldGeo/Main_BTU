# Generated by Django 3.2.1 on 2024-07-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='content',
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(default='no_cover.png', null=True, upload_to=''),
        ),
    ]