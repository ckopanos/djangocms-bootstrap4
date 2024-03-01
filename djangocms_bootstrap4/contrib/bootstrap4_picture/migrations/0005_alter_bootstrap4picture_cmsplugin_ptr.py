# Generated by Django 4.1.13 on 2024-03-01 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("bootstrap4_picture", "0004_auto_20190703_0831"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bootstrap4picture",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
    ]
