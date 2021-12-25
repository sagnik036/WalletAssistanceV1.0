
from django.db.models import query
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from .serializers import ExpenseSerializers
from .models import Expense
from rest_framework.response import Response
from .services import ExpenceService
from rest_framework import status

# Create your views here.

class ExpenseViewGetPost(GenericAPIView):
    serializer_class=ExpenseSerializers
    queryset=""

    @classmethod
    def get(self, request):       
        fetch,status_code=ExpenceService.fetchExpense()
        return Response(fetch,status_code)

    @classmethod
    def post(self,request):
        data=request.data
        postExpense,status_code = ExpenceService.post_updateExpense(data)
        return Response(postExpense,status_code)

class ExpenseViewUpdateDelete(GenericAPIView):
    serializer_class=ExpenseSerializers
    queryset=""

    @classmethod
    def get(self,request,pk=None):
        id=pk
        getExpenceById,status_code = ExpenceService.fetchExpense(id)
        return Response(getExpenceById,status_code)

    @classmethod
    def put(self,request,pk):
        id=pk 
        data=request.data
        updateExpense,status_code=ExpenceService.post_updateExpense(data,id)
        return Response(updateExpense,status_code)

    def delete(self,request,pk):
        delExpense,status_code=ExpenceService.deleteExpense(pk)
        return Response(delExpense,status_code)





