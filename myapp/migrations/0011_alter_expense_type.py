# Generated by Django 4.0 on 2021-12-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.CharField(choices=[('1', '1'), ('2', '2')], default='', max_length=50),
        ),
    ]
