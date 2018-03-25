from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from first_app import views

urlpatterns = [
    path('',views.index,name='index')
]
