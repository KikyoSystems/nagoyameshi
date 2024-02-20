from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('store_search/', views.StoreSearchView.as_view(), name='store_search')
]
