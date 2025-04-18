from django.urls import path
from . import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('nurses', views.nurses, name='nurse'),
    path('new_patient/', views.register_patient, name='register_patient'),

    path('doctors/', views.doctors, name='doctors'),
    path('ae/', views.ae, name='ae'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('accounts/', views.accounts, name='accounts'),
    path('hr/', views.hr, name='hr_page'),
    path('inventory/', views.inventory, name='inventory'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
