# Generated by Django 5.1.7 on 2025-03-15 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('symbol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('usd_value', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_currency_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destination_currency_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('exchange_date', models.DateTimeField(auto_now_add=True)),
                ('destination_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_currency', to='tradingbotweb.currency')),
                ('origin_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_currncy', to='tradingbotweb.currency')),
            ],
        ),
    ]
