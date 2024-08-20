

from rest_framework import serializers

from .models import *
class CompanyDetailsserializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = "__all__"

class Shopinfoserializers(serializers.ModelSerializer):
    class Meta:
        model = Shopinfo
        fields = "__all__"

class LogReportserializers(serializers.ModelSerializer):
    class Meta:
        model = LogReport
        fields = "__all__"