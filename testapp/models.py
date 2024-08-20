from django.db import models

# Create your models here.


class CompanyDetails(models.Model):
    companyname =  models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    contact =  models.CharField(max_length=200, default="")
    mailid = models.CharField(max_length=200, default="")
    website =  models.CharField(max_length=200, default="")
    instagramid = models.CharField(max_length=200, default="")
    twitterid =  models.CharField(max_length=200, default="")
    facebook = models.CharField(max_length=200, default="")
    linkedin =  models.CharField(max_length=200, default="")
    pinterest = models.CharField(max_length=200, default="")
    youtube = models.CharField(max_length=200, default="")
    printdetails = models.CharField(max_length=200, default="")


    class Meta:
        db_table = "CompanyDetails_tbl"
        ordering = ["id"] 

class Shopinfo(models.Model):
    cusid = models.CharField(max_length=200)
    shopname = models.CharField(max_length=200, default="")
    doorno =models.CharField(max_length=200, default="")
    area = models.CharField(max_length=200, default="")
    area2 =  models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    pincode =models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=200, default="")
    
    gstno =models.CharField(max_length=200, default="")
    fssai = models.CharField(max_length=200, default="")


    class Meta:
        db_table = "ShopInfo_tbl"
        ordering = ["id"] 

class LogReport(models.Model):
    cusid = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="")
    dt = models.DateTimeField(default="")
    description = models.CharField(max_length=200, default="")


    class Meta:
        db_table = "LogReport_tbl"
        ordering = ["id"] 

