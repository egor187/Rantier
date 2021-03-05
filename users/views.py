from django.shortcuts import render
from users.models import CustomUser
from django.views.generic import DetailView, ListView


class CustomUserListView(ListView):
    model = CustomUser
    # template_name =

class CustomUserDetailView(DetailView):
    model = CustomUser
    # template_name = pass