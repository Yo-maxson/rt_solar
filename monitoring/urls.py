from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ads/', views.AdsListView.as_view(), name='ads'),
    path('ads/<int:pk>', views.AdsDetailView.as_view(), name='ad_detail'),
    path('ads/add/', views.AdCreateView.as_view(), name='ad_create'),
    path('ads/<int:pk>/edit/', views.AdEditView.as_view(), name='ad_edit'),
              ]
