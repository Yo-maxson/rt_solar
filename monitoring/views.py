from django.shortcuts import render
from constance import config
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Vulnerability
from django.urls import reverse_lazy


def home_page(request):
    main_temp = {'title': 'Главная страница', 'turn_on_block': config.MAINTENANCE_MODE, }
    return render(request, 'main/index.html', context = main_temp)


class AdsListView(ListView):
    paginate_by = 2
    model = Vulnerability
    template_name = 'main/ad_list.html'
    context_object_name = 'ads_list'
    title_ads = {'title': 'Все объявления'}


    def get_queryset(self):
        return Vulnerability.objects.filter(relevance=True).order_by('date')


class AdsDetailView(DetailView):
    model = Vulnerability
    template_name = 'main/ad_detail.html'
    context_object_name = 'ad'


class AdCreateView(CreateView):
    model = Vulnerability
    fields = '__all__'
    template = 'ads_form.html'
    redirect_field_name = 'ads_list'
    success_url = reverse_lazy('ads_list')


class AdEditView(UpdateView):
    model = Vulnerability
    fields = '__all__'
    template = 'ads_form.html'
    redirect_field_name = 'ads_list'
    success_url = reverse_lazy('ads_list')