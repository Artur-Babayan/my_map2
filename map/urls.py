from django.urls import path
from map.views import index

urlpatterns = [
    path('', index, name='index'),

]