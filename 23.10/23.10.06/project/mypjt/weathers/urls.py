from django.urls import path
from . import views

app_name='weathers'
urlpatterns = [
    path('', views.index, name='index'),
    path('problem<int:num>/', views.problem, name='problem'),
    path('problem<int:num>/create/', views.create, name='create'),
    path('problem<int:num>/<int:pk>/delete/', views.delete, name='delete'),
    path('problem<int:num>/<int:pk>/update/', views.update, name='update'),
]