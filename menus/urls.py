from django.urls import path
from .views import menu_view

urlpatterns = [
    path('', menu_view),
    path('<slug:menu_url>/', menu_view),
    path('<slug:menu_url>/<path:rest_of_url>/', menu_view),
]