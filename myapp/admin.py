from django.contrib import admin
from django.db import models
from .models import Expense
from .models import Income
# Register your models here.

admin.site.register(Expense)
# admin.site.register(Income)

# class PersonDetailAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateField: {'input_formats': ('%m/%d/%Y',)},
#     }