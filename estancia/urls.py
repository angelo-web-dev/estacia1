from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='home'),
    path('cocina/', core_views.cocina, name='cocina'),
]
