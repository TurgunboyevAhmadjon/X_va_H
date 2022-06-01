from django.contrib import admin
from django.urls import path
from letters.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy, name="home"),
]
