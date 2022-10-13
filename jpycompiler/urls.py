""""---------------------------NITHISH--KUMARAN-S--------------------------------
MADE BY : ------ NITHISH KUMARAN .K.C.S ------
20BCAR0116
NITHISHKUMARAN1@GMAIL.COM
PROJECT @ JU(20BCAR0116)-PCL 2022-2023 copyright-c."""
from django.urls import path, include

# import views

from . import views

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('runcode', views.runcode, name="runcode"),

]

