# Generated by Django 4.0 on 2021-12-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='catagory',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('5', '5'), ('6', '6'), ('4', '4')], default='', max_length=50),
        ),
    ]
