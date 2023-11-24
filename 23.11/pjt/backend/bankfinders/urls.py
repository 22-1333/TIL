from django.urls import path
from bankfinders import views


urlpatterns = [
    path('nearest_bank/', views.nearest_bank)
]
