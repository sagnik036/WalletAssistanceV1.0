
from django.urls import path,include

urlpatterns = [
    path('Expense/',
     include("myapp.Expenses.urls")
    ),

    # path('Income/',
    #  include("myapp.Income.urls")    
    # ),
]