from django.urls import path
from . import views

urlpatterns = [
    path('deposit_list/', views.deposit_list),
    path('installment_saving_list/', views.installment_saving_list),
    path('<str:fin_prdt_cd>/', views.detail)
]
