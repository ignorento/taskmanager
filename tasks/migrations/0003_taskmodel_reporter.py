# Generated by Django 4.2.2 on 2023-07-11 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_rename_task_taskmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
