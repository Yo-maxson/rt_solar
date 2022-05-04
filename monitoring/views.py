from django.shortcuts import render
from constance import config
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Vulnerability
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect


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


class AdCreateView(CreateView):
    model = Vulnerability
    fields = '__all__'
    template = 'monitoring/ads_form.html'
    redirect_field_name = 'ads_list'
    success_url = reverse_lazy('ads_list')


# class AdCreateView(CreateView):
#     model = Vulnerability
#     fields = '__all__'
#     template = 'ads_form.html'
#     redirect_field_name = 'ads_list'
#     success_url = reverse_lazy('ads_list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form = self.get_form()
#         if form.is_valid():
#             self.object = form.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.form_invalid(form)


class AdEditView(UpdateView):
    model = Vulnerability
    fields = '__all__'
    template = 'monitoring/ads_form.html'
    redirect_field_name = 'ads_list'
    success_url = reverse_lazy('ads_list')
