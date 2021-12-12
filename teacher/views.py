from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from teacher.forms import CustomUserCreationForm

# Create your views here.


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
