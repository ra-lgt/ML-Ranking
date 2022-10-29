from . import views
from django.urls import path

urlpatterns = [
    path('',views.search_bus),
    path('bus_filter_Ac',views.bus_filter_Ac),
    path('bus_filter_Nc',views.bus_filter_Nc),
    path('bookseats/<starting>',views.bookseats),


    #path('passenger',views.passenger),


    ]
