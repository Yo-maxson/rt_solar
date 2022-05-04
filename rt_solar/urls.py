from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from monitoring.views import e_handler404

handler404 = e_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring.urls')),


]

# handler404 = "main.views.page_not_found_view"
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)