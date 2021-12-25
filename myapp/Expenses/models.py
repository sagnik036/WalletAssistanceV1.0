
from django.db import models
from project import settings

#models for Expenses

#category
# 1.Electronics
# 2.FastFood
# 3.Salary
# 4.Bonus
# 5.Travel
# 6.Other 
CATAGORY={
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6')
}

#1 for expense
#2 for income
TYPE={
    ('1','1'),
    ('2','2')
    
}

class Expense(models.Model):
    Name=models.CharField(
        max_length=20
    )
    
    published_date=models.DateTimeField(
        auto_now=True
    )

    created_date=models.DateTimeField(
        null=True
    )
    description=models.TextField(
        max_length=100,
        null=True
    )

    catagory=models.CharField(
        max_length=50,
        choices=CATAGORY,
        null=True
    )

    type=models.CharField(
        max_length=50,
        choices=TYPE,
        default=''

    )
    expence=models.FloatField(
        default=0,
        null=True
    )

    income=models.FloatField(
        default=0,
        null=True
    )

    def __str__(self):
        return self.Name