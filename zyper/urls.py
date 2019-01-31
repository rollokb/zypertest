from django.urls import path
from zyper.images import views

urlpatterns = [
    path('', views.index)
]
