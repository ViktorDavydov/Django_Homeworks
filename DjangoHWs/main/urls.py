from django.urls import path

from DjangoHWs.main.views import index

urlpatterns = [
    path('', index)
]
