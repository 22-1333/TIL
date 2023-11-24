from django.urls import path
from . import views

urlpatterns = [
    path('deposit_list/', views.deposit_list),
    path('installment_saving_list/', views.installment_saving_list),

    path('recommend_deposit_product/<str:username>/', views.recommend_deposit_product),
    path('product/<str:fin_prdt_cd>/', views.product_detail),
    
    path('get_registered_list/<int:type>/<str:username>/', views.get_registered_list),
    path('register/<str:fin_prdt_cd>/<str:username>/', views.register),
    path('<str:fin_prdt_cd>/', views.detail),
]
