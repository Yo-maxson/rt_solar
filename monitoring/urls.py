from django.urls import path, include
from . import views

app_name = 'monitoring'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ads/', views.AdsListView.as_view(), name='ads_list'),
    path('ads/<int:pk>', views.AdsDetailView.as_view(), name='ad_detail'),
    path('ads/add/', views.AdCreateView.as_view(), name='ad_create'),
    path('ads/<int:pk>/edit/', views.AdEditView.as_view(), name='ad_edit'),
    path('ads/<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_del'),

              ]
