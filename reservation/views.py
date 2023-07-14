from django.shortcuts import render
from .models import Reservation, Table, ReservationContact
from .forms import ReservationForm
from django.contrib import messages
from django.core.mail import send_mail


def reservation_view(request):
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
                successful_message = 'Table "{}" is successfully reserved at "{}" on "{}" for you.'.format(table.name,
                                                                                                           time.strftime(
                                                                                                               '%H:%M'),
                                                                                                           date)
                messages.add_message(request, messages.SUCCESS, successful_message)

                send_mail(
                    "Restaurant Reservation", successful_message, "info@mahyarnazari.ir", [request.user.email],
                    fail_silently=False,)
            else:
                messages.add_message(request, messages.ERROR,
                                     'There are no empty tables at this time. Please choose another time.')

        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, messages.ERROR, error)

    context = {'reservation_info': reservation_info}
    return render(request, 'reservation/reservation.html', context=context)
