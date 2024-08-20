from django.shortcuts import render

from rest_framework import viewsets

from .models import *
from .Serillizer import  *
from rest_framework import pagination

# Create your views here.

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class CompanyDetailsView(viewsets.ModelViewSet):
    queryset = CompanyDetails.objects.all()
    serializer_class = CompanyDetailsserializers


class ShopinfoView(viewsets.ModelViewSet):
    queryset = Shopinfo.objects.all()
    serializer_class = Shopinfoserializers
    pagination_class = CustomPagination

class LogReportView(viewsets.ModelViewSet):
    queryset = LogReport.objects.all()
    serializer_class = LogReportserializers
    pagination_class = CustomPagination
