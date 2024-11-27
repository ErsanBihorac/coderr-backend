# Generated by Django 5.1.3 on 2024-11-27 12:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_alter_offer_created_at_alter_offer_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdetail',
            name='offer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='offers.offer'),
        ),
        migrations.AlterField(
            model_name='offerdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='offerdetail',
            name='revisions',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-1)]),
        ),
        migrations.AlterField(
            model_name='offerdetail',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='offerdetail',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]