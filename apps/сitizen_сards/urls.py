from django.urls import path
from .views import CitizenCardListView, CitizenCardDetailView, CitizenCardCreateView

urlpatterns = [
    path('', CitizenCardListView.as_view(), name='citizen_card_list'),
    path('<int:pk>/', CitizenCardDetailView.as_view(), name='citizen_card_detail'),
    path('create/', CitizenCardCreateView.as_view(), name='citizen_card_create'),
]
