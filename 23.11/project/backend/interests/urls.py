from django.urls import path
from . import views

urlpatterns = [
    path('deposit_list/', views.deposit_list),
    path('installment_savings_list/', views.installment_saving_list)
]
