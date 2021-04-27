from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from ClientReg.models import ClientInfo


# Create your views here.
def clientRegPage(request):
    return render(request, '[CLIENTREG]home.html')


def clientRegProcess(request):
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

        if (username_client== "" or firstName_client== "" or lastName_client=="" or email_client=="" or password_client=="" or conditions_client=="" or confirmation_client=="" or dob_client=="" or height_client=="" or weight_client=="" ):
            messages.add_message(request, messages.INFO, 'Please fill all fields in')
            return redirect('/clientRegPage')

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
                response = HttpResponse(render(request, 'clientPage.html', {'client_person': client_person}))
                response.set_cookie('username', username_client)
                return response

        else:
            messages.info(request, 'passwords are not matching')

            return redirect('/')
