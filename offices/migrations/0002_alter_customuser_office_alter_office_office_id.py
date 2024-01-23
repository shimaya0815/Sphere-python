# Generated by Django 4.2.7 on 2024-01-13 19:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offices.office'),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_id',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
