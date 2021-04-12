from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


from django.http import HttpResponse
# Create your views here.
from health.models import ClientInfo


def home(request):
    return render(request, 'home.html')

def client(request):

    if request.method == 'POST':
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
            if ClientInfo.objects.filter(name=firstName_client).exists():
                messages.add_message(request, messages.INFO, 'name is taken')
                return redirect('/')

            else:

                client_person = ClientInfo(name=firstName_client,
                                           family=lastName_client,
                                           birth=dob_client,
                                           confirmation=confirmation_client,
                                           password=password_client,
                                           conditions=conditions_client
                                           )
                client_person.save()
                return render(request, 'clientPage.html')

        else:
            messages.info(request, 'passwords are not matching')

            return redirect('/')



def doctor(request):
    return render(request, 'doctorPage.html')