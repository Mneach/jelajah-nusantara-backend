# Generated by Django 4.2.3 on 2024-02-29 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('island', '0001_initial'),
        ('province', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='island',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='island.island'),
        ),
    ]