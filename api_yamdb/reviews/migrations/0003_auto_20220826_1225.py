# Generated by Django 2.2.16 on 2022-08-26 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220825_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rate',
            new_name='score',
        ),
    ]
