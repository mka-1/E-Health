from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django import forms
from .models import ConfirmedAppointment
from .forms import Apptform
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.http import HttpResponse
# Create your views here.

from ClientReg.models import ClientInfo
from DoctorReg.models import DoctorInfo


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def create_view(request):
    context = {}

    form = Apptform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appt")

    context['form'] = form
    return render(request, "create_view.html", context)


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = ConfirmedAppointment.objects.get(id=id)

    return render(request, "detail_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = ConfirmedAppointment.objects.all()

    return render(request, "list_view.html", context)


def list_view_admin(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = ConfirmedAppointment.objects.all()

    return render(request, "list_view_admin.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(ConfirmedAppointment, id=id)

    # pass the object as instance in form
    form = Apptform(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appt")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(ConfirmedAppointment, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/appt")

    return render(request, "delete_view.html", context)


def client(request):
    if request.method == 'POST':
        username_client = request.POST['username']
        firstName_client = request.POST['exampleInputName1']
        lastName_client = request.POST['exampleInputFamily1']
        email_client = request.POST['exampleInputEmail1']
        password_client = request.POST['exampleInputPassword1']
        confirmation_client = request.POST['confirmation1']
        conditions_client = request.POST['exampleInputConditions1']
        dob_client = request.POST['exampleInputDate1']
        height_client = request.POST['exampleInputHeight1']
        weight_client = request.POST['exampleInputWeight1']

        if password_client == confirmation_client:
            if ClientInfo.objects.filter(email=email_client).exists():
                messages.add_message(request, messages.INFO, 'email is taken')
                return redirect('/')


            elif ClientInfo.objects.filter(username=username_client).exists():
                messages.add_message(request, messages.INFO, 'username is taken')
                return redirect('/')
            else:

                client_person = ClientInfo(username=username_client,
                                           name=firstName_client,
                                           family=lastName_client,
                                           birth=dob_client,
                                           confirmation=confirmation_client,
                                           password=password_client,
                                           conditions=conditions_client,
                                           height=height_client,
                                           weight=weight_client
                                           )
                client_person.save()
                return render(request, 'clientPage.html', {'clientObj': client_person})

        else:
            messages.info(request, 'passwords are not matching')

            return redirect('/')


def doctor(request):
    if request.method == 'POST':
        firstName_doctor = request.POST['exampleInputName2']
        lastName_doctor = request.POST['exampleInputFamily2']
        email_doctor = request.POST['exampleInputEmail2']
        password_doctor = request.POST['exampleInputPassword2']
        confirmation_doctor = request.POST['confirmation2']
        specs_doctor = request.POST['exampleInputSpeci1']
        hospitals = request.POST['Hospital']

        if password_doctor == confirmation_doctor:
            if DoctorInfo.objects.filter(firstname=firstName_doctor).exists():  # see if username exists basically
                messages.add_message(request, messages.INFO, 'name is taken')
                return redirect('/')

            else:

                doctor_person = DoctorInfo(firstname=firstName_doctor,
                                           lastname=lastName_doctor,
                                           specialization=specs_doctor,
                                           confirmation=confirmation_doctor,
                                           password=password_doctor,
                                           emailDr=email_doctor,
                                           hospital=hospitals
                                           )
                doctor_person.save()
                return render(request, 'doctorPage.html')

        else:
            messages.add_message(request, messages.INFO, 'passwords are not matching')

            return redirect('/')
    return render(request, 'doctorPage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['usernameLogin']
        password = request.POST['passwordLogin']

        if ClientInfo.objects.filter(username=username, password=password).exists():
            return render(request, 'ClientPage.html')
        else:
            messages.add_message(request, messages.INFO, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')
