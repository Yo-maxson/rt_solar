from django.shortcuts import render
from constance import config
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Vulnerability
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateAdForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


def home_page(request):
    main_temp = {'title': 'Главная страница', 'turn_on_block': config.MAINTENANCE_MODE, }
    return render(request, 'monitoring/index.html', context=main_temp)


class AdsListView(ListView):
    paginate_by = 2
    model = Vulnerability
    template_name = 'monitoring/ad_list.html'
    context_object_name = 'ads_list'
    title_ads = {'title': 'Все объявления'}

    def get_queryset(self):
        return Vulnerability.objects.filter(relevance=True).order_by('date')


class AdsDetailView(DetailView):
    model = Vulnerability
    template_name = 'monitoring/ad_detail.html'
    context_object_name = 'ad'


class AdCreateView(LoginRequiredMixin, CreateView):
    template_name = 'monitoring/ads_form.html'
    # form_class = CreateAdForm
    model = Vulnerability
    fields = [
        'name', 'title', 'text', 'date'
    ]

    success_url = reverse_lazy('monitoring:ads_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class AdEditView(LoginRequiredMixin, UpdateView):
    template_name = 'monitoring/ads_form.html'
    model = Vulnerability
    fields = [
        'name', 'title', 'text', 'date'
    ]

    success_url = reverse_lazy('monitoring:ads_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user != obj.author:
            raise PermissionDenied()
        return obj


class AdDeleteView(LoginRequiredMixin, DeleteView):
    model = Vulnerability
    success_url = reverse_lazy('monitoring:ads_list')
    template_name = 'monitoring/ad_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user != obj.author:
            raise PermissionDenied()
        return obj
