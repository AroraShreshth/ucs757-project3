from django.shortcuts import render
from django.contrib.auth import views as auth_views
from proj.settings import website_name
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, UserLoginForm)

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('dashboard-home')
    return render(request, 'unlogged/index.html', {'title': '', 'website_name': website_name})


# class DashBoard(LoginRequiredMixin, TemplateView):
#     template_name = 'dashboard/home.html'

#     # def get(self, request, *args, **kwargs):
#     #     context = self.get_context_data(**kwargs)
#     #     if not request.user.profile.setup:
#     #         return redirect('dashboard-welcome')
#     #     return self.render_to_response(context)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['website_name'] = website_name
#         context['title'] = 'Dashboard'
#         return context

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            # messages.success(
            #     request, f' {username} your account has been crreated successfully')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard-home')
        form = UserRegisterForm()
    return render(request, 'unlogged/register.html', {'website_name': website_name, 'title': 'Register', 'form': form})

class NewLoginView(auth_views.LoginView):
    template_name = 'unlogged/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Login'
        context['form'] = UserLoginForm
        return context

