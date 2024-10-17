# Generated by Django 5.0.6 on 2024-10-16 06:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0011_cartitemmodel"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitemmodel",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="cart_item_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
