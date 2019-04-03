from django.urls import path
from shopapp.views import base_view

urlpatterns = [
    path('', base_view, name='base'),
]
