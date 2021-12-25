# Generated by Django 4.0 on 2021-12-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_income_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='cost',
        ),
        migrations.AddField(
            model_name='expense',
            name='expence',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='income',
            field=models.FloatField(default=0, null=True),
        ),
    ]
