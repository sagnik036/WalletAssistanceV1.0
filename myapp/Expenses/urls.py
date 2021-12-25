from django.contrib import admin
from django.urls import path,include

from  myapp.Expenses import views
from myapp.Expenses.services import ExpenceService


urlpatterns = [
    path('get&post/',
     views.ExpenseViewGetPost.as_view()
    ),

    path('updateDelete/<int:pk>/',
     views.ExpenseViewUpdateDelete.as_view()
    ), 

    path('filterExpense/',include("myapp.Expenses.FilterExpense.urls")),

    
  ]