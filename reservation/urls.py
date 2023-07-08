from django.urls import path, include
from reservation.views import *


app_name = 'reservation'
urlpatterns = [
    path('', reservation_view, name='reservation'),

]
