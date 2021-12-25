from django.db.models import fields
from django.db.models.base import Model
from .models import Expense
from rest_framework import serializers

class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields="__all__"
