from django.urls import path
from apartments.views import ApartmentsIndexView, ApartmentsDetailView, ApartmentsUpdateView, ApartmentsCreateView, ApartmentsDeleteView

app_name = 'apartments'

urlpatterns = [
    path('', ApartmentsIndexView.as_view(), name='apartment_index'),
    path('<int:pk>/', ApartmentsDetailView.as_view(), name='apartment_detail'),
    path('<int:pk>/update/', ApartmentsUpdateView.as_view(), name='apartment_update'),
    path('<int:pk>/delete/', ApartmentsDeleteView.as_view(), name='apartment_delete'),
    path('create/', ApartmentsCreateView.as_view(), name='apartment_create'),
]