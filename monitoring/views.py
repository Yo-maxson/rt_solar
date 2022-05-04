from constance import config
from django.shortcuts import render, HttpResponseRedirect


def e_handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def home_page(request):
    main_temp = {'title': 'Главная страница', 'turn_on_block': config.MAINTENANCE_MODE, }
    return render(request, 'main/index.html', context=main_temp)
