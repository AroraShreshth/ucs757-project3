from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from .models import ModelCall
from .forms import MLCallImageForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
website_name = 'ML Library'

@login_required
def fDashBoard(request):
    
    if request.method == 'POST':
        form = MLCallImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard-list')

    return render(request, 'dashboard/home2.html', {'website_name': website_name, 'title':'Dashboard','form': MLCallImageForm})

class DashBoard(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/home2.html'
    model = ModelCall
    fields = ['image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Dashboard'
        return context

    def get_success_url(self):
        return reverse('dashboard-list')

class CallList(LoginRequiredMixin, ListView):
    template_name = 'dashboard/list.html'
    model = ModelCall
    context_object_name ='mlcalls'
    ordering = ['-created_date']
    paginate_by = 20

    def get_queryset(self):
        new_context = ModelCall.objects.filter(user=self.request.user)
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'ML Library Calls'
        context['count'] = self.get_queryset().count()
        return context



class TriggerEmotion(LoginRequiredMixin, DetailView):
    model = ModelCall
    template_name = 'dashboard/trigger_emotion.html'
    context_object_name = 'mlcall'

    def get(self, request, *args, **kwargs):
        mlcall = self.get_object()
        mlcall.getemo()
        return redirect('dashboard-list')
    
class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ModelCall
    template_name = 'dashboard/deleteview.html'
    context_object_name = 'mlcall'

    def test_func(self):
        mlcall = self.get_object()
        return self.request.user == mlcall.user

    def get_success_url(self):
        return reverse_lazy('dashboard-list')

@login_required
def ImageUpload(request):

    if request.method == 'POST':
        form = MLCallImageForm(request.POST, request.FILES, instance=request.user)
        form.instance.user = request.user

        if form.is_valid():
            form.save()

    return redirect('dashboard-list')