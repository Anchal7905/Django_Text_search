# api/urls.py
from django.urls import path
from .views import TextSearchView

urlpatterns = [
    path('search/', TextSearchView.as_view(), name='text-search'),
]
