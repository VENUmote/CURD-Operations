from django.urls import path
from . import views

urlpatterns = [
    path('',views.view, name='view'),
    path('cols/create/',views.create, name='create'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('cols/<int:pk>/edit/', views.edit, name='edit'),
    path('cols/<int:pk>/delete', views.delete, name='delete'),
    path('venu/', views.venu, name='venu')

]