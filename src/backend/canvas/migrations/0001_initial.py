# Generated by Django 3.1.4 on 2021-01-05 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=14,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Room Name")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created At"
                    ),
                ),
                ("is_live", models.BooleanField(default=False, verbose_name="Live")),
                (
                    "duration",
                    models.IntegerField(null=True, verbose_name="Duration (in sec)"),
                ),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hosted",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="participated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
