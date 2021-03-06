from django.urls import path
from apartments.views import ApartmentsIndexView, ApartmentsDetailView, ApartmentsUpdateView, ApartmentsCreateView

app_name = 'apartments'

urlpatterns = [
    path('', ApartmentsIndexView.as_view(), name='apartment_index'),
    path('<int:pk>/', ApartmentsDetailView.as_view(), name='apartment_detail'),
    path('<int:pk>/update/', ApartmentsUpdateView.as_view(), name='apartment_update'),
    path('create/', ApartmentsCreateView.as_view(), name='apartment_create'),
]