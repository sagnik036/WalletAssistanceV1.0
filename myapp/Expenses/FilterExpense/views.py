from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db.models import Sum
from myapp.Expenses.models import Expense
from myapp.serializers import ExpenseSerializers
from .serializers import FilterExpenseSerializers

# Create your views here.

class FilterExpenseYearView(GenericAPIView):
    serializer_class=FilterExpenseSerializers
    queryset=""

    @classmethod
    def get(self,request,year):
     try:  
        filterExpense = Expense.objects.filter(created_date__year=year).order_by('-id')
        if filterExpense:
          serializer=FilterExpenseSerializers(
            filterExpense,
            many=True
          )
          status_code=200
          return Response(serializer.data,status_code)
        else:
         status_code=400
         response=[{"RESULT":"ENTER PROPER YEAR"}]
         return Response(response,status_code)
     except:
         status_code=400
         response=[{"RESULT":"ENTER PROPER YEAR"}]
         return Response(response,status_code)

class CalculateTotal(GenericAPIView):
    serializers_class=''
    queryset=''

    @classmethod
    def get(self,request):
     try:
        income=Expense.objects.aggregate(Sum('income'))
        expence=Expense.objects.aggregate(Sum('expence'))
        for i in income:
            income=income[i]
        for k in expence:
            expence=expence[k]
        wallet_balance=income-expence
        status_code=200
        response=[{'TOTAL_INCOME':income},{'TOTAL_EXPENSE':expence},{'BALANCE':wallet_balance}]
        return Response(response,status_code)
     except:
         status_code=400
         response=[{"RESULT":"NO_DATA_FOUND"}]
         return Response(response,status_code)

class FilterByCatagory(GenericAPIView):
    serializers_class=''
    queryset=''

    @classmethod
    def get(self,request,catagory):
     try:  
        filterCatagory = Expense.objects.filter(catagory=catagory).order_by('-id')
        if filterCatagory:
          serializer=FilterExpenseSerializers(
            filterCatagory,
            many=True
          )
          status_code=200
          return Response(serializer.data,status_code)
        else:
         status_code=400
         response=[{"RESULT":"CHOOSE CORRECTLY"}]
         return Response(response,status_code)
     except:
         status_code=400
         response=[{"RESULT":"CHOOSE CORRECTLY"}]
         return Response(response,status_code)


class FilterByType(GenericAPIView):
    serializers_class=''
    queryset=''

    @classmethod
    def get(self,request,type):
     try:  
        filterType = Expense.objects.filter(type=type).order_by('-id')
        if filterType:
          serializer=FilterExpenseSerializers(
            filterType,
            many=True
          )
          status_code=200
          return Response(serializer.data,status_code)
        else:
         status_code=400
         response=[{"RESULT":"CHOOSE CORRECTLY"}]
         return Response(response,status_code)
     except:
         status_code=400
         response=[{"RESULT":"CHOOSE CORRECTLY"}]
         return Response(response,status_code)

