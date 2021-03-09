from django.urls import path
from tenants.views import tenants_index_view, tenant_create_view, TenantDeleteView, TenantDetailView, TenantUpdateView


app_name = 'tenants'

urlpatterns = [
    path('', tenants_index_view, name='tenant_index'),
    path('<int:pk>/', TenantDetailView.as_view(), name='tenant_detail'),
    path('create/', tenant_create_view, name='tenant_create'),
    path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
    path('<int:pk>/update/', TenantUpdateView.as_view(), name='tenant_update'),
]