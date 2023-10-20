from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gen_select_html/', views.error_page, name='error_page'),
]