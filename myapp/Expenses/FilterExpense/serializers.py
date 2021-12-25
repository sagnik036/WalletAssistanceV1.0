from django.db.models import fields
from rest_framework import serializers
from .models import *
class FilterExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields="__all__"