from django.contrib import admin
from django.urls import path,include

from myapp.Expenses import views
from  myapp.Expenses.FilterExpense import views



urlpatterns = [
    path('year=<int:year>/',
     views.FilterExpenseYearView.as_view()
    ),

    path('Calculate/',
     views.CalculateTotal.as_view()
    ),

    path('catagory=<int:catagory>/',
     views.FilterByCatagory.as_view()
    ),

    path('type=<int:type>/',
     views.FilterByType.as_view()
    ),

]