# Generated by Django 2.2.1 on 2019-11-11 21:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="account",
        ),
        migrations.DeleteModel(
            name="Account",
        ),
    ]
