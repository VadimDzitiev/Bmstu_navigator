# Generated by Django 4.2.7 on 2023-11-13 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='requestservice',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='request',
            table='requests',
        ),
        migrations.AlterModelTable(
            name='requestservice',
            table='M-M',
        ),
        migrations.AlterModelTable(
            name='service',
            table='service',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='users',
        ),
    ]