from django.contrib import admin
from django.urls import path
from gen import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView, name="home"),
    path('cashapp', views.Geneview, name="generate"),
    path('reciept', views.paymentview, name="payment"),
    path('success', views.Success, name="suc"),
    path('summary', views.pay, name="sum"),
    path('payment-sent', views.Lastview, name="sent"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)