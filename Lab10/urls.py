# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', views.CompanyDetailAPIView.as_view(), name='company-detail'),
    path('vacancies/', views.VacancyListCreateAPIView.as_view(), name='vacancy-list-create'),
    path('vacancies/<int:pk>/', views.VacancyDetailAPIView.as_view(), name='vacancy-detail'),
]
