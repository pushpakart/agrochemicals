from django.urls import path
from .views import (ChemicalListView, ChemicalCreateView, 
                   ChemicalUpdateView, ChemicalDeleteView,
                   ChemicalDetailView)

app_name = 'inventory'

urlpatterns = [
    path('', ChemicalListView.as_view(), name='chemical-list'),
    path('new/', ChemicalCreateView.as_view(), name='chemical-create'),
    path('<int:pk>/', ChemicalDetailView.as_view(), name='chemical-detail'),
    path('<int:pk>/edit/', ChemicalUpdateView.as_view(), name='chemical-update'),
    path('<int:pk>/delete/', ChemicalDeleteView.as_view(), name='chemical-delete'),
]