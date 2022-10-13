""""---------------------------NITHISH--KUMARAN-S--------------------------------
MADE BY : ------ NITHISH KUMARAN .K.C.S ------
20BCAR0116
NITHISHKUMARAN1@GMAIL.COM
PROJECT @ JU(20BCAR0116)-PCL 2022-2023 copyright-c."""
from django.urls import path, include

# import views

from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('runcode', views.runcode, name="runcode"),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='Home'),
    path('blog/', include("blog.urls")),
    path('shop/', include("shop.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
