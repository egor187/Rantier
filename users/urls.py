from django.urls import path
from .views import CustomUserDetailView, CustomUserIndexView, CustomUserCreateView, CustomUserUpdateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('', CustomUserIndexView.as_view(), name='user_index'),
    path('<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('create/', CustomUserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(), name='user_update'),
]