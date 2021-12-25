from django.db import models
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from .serializers import ExpenseSerializers
from .models import Expense
from rest_framework.response import Response
from django.views import View
from rest_framework.status import HTTP_400_BAD_REQUEST


class ExpenceService(View):
    
    @staticmethod
    def getqueryset(id=None):
     if id:
         fetchExpenceByid=Expense.objects.get(pk=id)
         print(fetchExpenceByid)
         return fetchExpenceByid
     else:
        getAllExpence=Expense.objects.all().order_by('-id')
        return getAllExpence

    @staticmethod
    def fetchExpense(id=None):
     
        if id:

         try:
            queryset=ExpenceService.getqueryset(id)
            serializer=ExpenseSerializers(
                queryset
            )
            status_code=200
            return serializer.data,status_code
        
         except:
            status_code=400
            return f"NOT FOUND",status_code

        else:
          queryset = ExpenceService.getqueryset()
          serializer = ExpenseSerializers(
              queryset, 
              many=True
            )
          status_code=200
        return serializer.data,status_code


    @staticmethod
    def post_updateExpense(data,id=None):
      print(id)
      if id:
        fetchExpensebyID=ExpenceService.getqueryset(id)
        print(fetchExpensebyID)
        serializer=ExpenseSerializers(
            fetchExpensebyID,
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            status_code=200
            return serializer.data,status_code
        else:
            status_code=400
            return serializer.errors,status_code
    
      else:
        serializer = ExpenseSerializers(
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            status_code=200
            return serializer.data,status_code
        else:
            status_code=400
            return serializer.errors,status_code
    
    @staticmethod
    def deleteExpense(id):
        try:
         fetchExpense=ExpenceService.getqueryset(id)
         if fetchExpense:
             fetchExpense.delete()
             status_code=200
             return f"DELETED",status_code
         else:
             status_code=400
             return f"NO Expense FOUND AT WITH THIS ID",status_code

        except:
            status_code=400
            return f"NO Expense FOUND WITH THIS ID",status_code
