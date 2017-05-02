from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import viewsets
from Capstone_TWF.settings import LOGOUT_REDIRECT_URL

from accounts.forms import MemberRegistration
from accounts.models import Member
from accounts.serializers import GroupSerializer, MemberSerializer


# from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'GET':
        form = MemberRegistration()
        context = {'form': form}
        return render(request, 'site.html', context)

    elif request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            authlogin(request, user)
            return redirect('/app')  # entrance door to app - redirect
            # Redirect to a success page.

        else:
            messages.error(request, message="Credentials are not valid, please re-enter or register.")
            return redirect('/accounts/login')

            # Return an 'invalid login' error message.


def registration(request):
    if request.method == 'POST':
        #TODO; handle errors

        form = MemberRegistration(data=request.POST)

        if form.is_valid():

            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            phone = request.POST['phone']
            # email = request.POST['email']
            member = Member.objects.create_user(username=username, password=password1, phone=phone)

            messages.success(request, message="Account Created Successfully, Please Login!")
            return redirect(reverse('/accounts/login/'))

        else:
            context = {'form': form}
            return render(request, 'site.html', context)

        # Return an 'invalid login' error message.


@login_required(login_url='/accounts/login/')
def app(request):
    context = {}
    return render(request, 'app.html', context)


def logout_view(request):
    logout(request)
    return redirect(LOGOUT_REDIRECT_URL)

# def forgot_password(request):
#     if request.method == 'GET':
#
#         form = MemberForgotPassword()
#
#     elif request.method == 'POST':
#
#         form = MemberForgotPassword(data=request.POST)
#
#         if form.is_valid():
#             change_password = form.save(commit=False)
#             change_password.save()
#
#     context = {'form': form}
#
#     return render(request, 'forgot_page.html', context)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
