from django.urls import path
from collector import views

urlpatterns=[
    path('milk_collections/add/', views.AddMilkCollection)
]