from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Reservation, Table, ReservationContact, Background
from .forms import ReservationForm
from django.contrib import messages
from datetime import datetime


def reservation_view(request):
    background = Background.objects.all()
    reservation_info = ReservationContact.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            changed_form = form.save(commit=False)
            count = form.cleaned_data['count']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            reserved = Reservation.objects.filter(date=date, time=time)
            table = Table.objects.exclude(id__in=
                                          reserved.values_list('table_id', flat=True)).filter(min_seats__lte=count,
                                                                                              max_seats__gte=count).first()
            if table:
                changed_form.table = table
                changed_form.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Table "{}" is successfully reserved at "{}" on "{}" for you.'.format(table.name,
                                                                                                           time.strftime(
                                                                                                               '%H:%M'),
                                                                                                           date))
            else:
                messages.add_message(request, messages.ERROR,
                                     'There are no empty tables at this time. Please choose another time.')


        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, messages.ERROR, error)

    context = {'reservation_info': reservation_info, 'background': background}
    return render(request, 'reservation/reservation.html', context=context)
