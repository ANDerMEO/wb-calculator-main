# Generated by Django 4.1.3 on 2022-12-04 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_alter_warehouse_free_space_alter_warehouse_space'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehouse',
            old_name='free_space',
            new_name='occupied_space',
        ),
    ]
