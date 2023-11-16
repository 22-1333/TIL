from django.urls import path
from . import views

urlpatterns = [
    path('<str:cur_unit>/', views.exchange_calculator),
]
