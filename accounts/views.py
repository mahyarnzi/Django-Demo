from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


# Create your views here.
def login_view(request):
    next = ''
    if request.GET:
        if 'next' in request.GET:
            next = request.GET['next']

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
            else:
                messages.add_message(request, messages.ERROR, 'Username or Password is not correct. Try again ...')
        else:
            messages.add_message(request, messages.ERROR, 'Username or Password is not correct. Try again ...')
        if next != "":
            return HttpResponseRedirect(next)
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'You have successfully registered.')
                return redirect('accounts:login')

            else:
                if form.errors:
                    for field in form:
                        for error in field.errors:
                            messages.add_message(request, messages.ERROR, error)

        return render(request, 'accounts/signup.html')
    else:
        messages.add_message(request, messages.ERROR, "If you want to sign up, you must sign out first.")
        return redirect('accounts:login')


##########################  Reset Password  ###############################
class CustomPasswordResetView(PasswordResetView):
    from_email = 'IT@mahyarnazari.ir'
    template_name = 'accounts/resetpassword/password_reset.html'
    email_template_name = 'accounts/resetpassword/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/resetpassword/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/resetpassword/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/resetpassword/password_reset_complete.html'
