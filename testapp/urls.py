from django.urls import path,include
from . import views
from rest_framework import routers
from testapp.views import *

router = routers.DefaultRouter()


router.register("CompanyDetails", CompanyDetailsView, basename="CompanyDetails")
router.register("Shopinfo", ShopinfoView, basename="Shopinf")

# Settings
router.register("LogReport", LogReportView, basename="LogReport")

urlpatterns = [
    path("",include(router.urls))
]