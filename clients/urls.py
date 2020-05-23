from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    PurchasedCarUpdateView,
    PurchasedCarDeleteView,
    PurchasedCarCreatView,
    CommentCreateView
)

urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('purchasedCar/<int:pk>/edit/', PurchasedCarUpdateView.as_view(), name='purchasedCar_edit'),
    path('purchasedCar/<int:pk>/delete/', PurchasedCarDeleteView.as_view(), name='purchasedCar_delete'),
    path('purchasedCar/new/', PurchasedCarCreatView.as_view(), name='purchasedCar_new'),
    path('comment/new/', CommentCreateView.as_view(), name='comment_new')

]
