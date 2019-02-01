from django.urls import path
from zyper.images import views


urlpatterns = [
    path('images/', views.image_list, name='list'),
    path('images/<int:pk>/', views.image_instance, name='instance'),
]
