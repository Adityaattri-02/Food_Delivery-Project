from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    path('',index),
    path('getdata',getdata),
    path('about/',about),
    path('blog_details/',blog),
    path('cart_view/',cart),
    path('check_out/',checkout),
    path('contact/',contact),
    path('dashboard/',dashboard),
    path('header/',header),
    path('footer/',footer),
    path('menu/',menu),
    path('payment/',payment),
    path('sign_in/',signin),
    path('sign_up/',signup),
    path('demo/',demo)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)