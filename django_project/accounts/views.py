from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CustomUserCreationForm


# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm     # which form should I use to create user
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
