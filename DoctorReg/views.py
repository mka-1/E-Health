from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from DoctorReg.models import DoctorInfo
from health.models import ConfirmedAppointment


def doctorRegPage(request):
    return render(request, '[DOCTORREG]home.html')

def doctorRegProcess(request):
    if request.method == 'POST':
        firstName_doctor = request.POST['exampleInputName2']
        lastName_doctor = request.POST['exampleInputFamily2']
        email_doctor = request.POST['exampleInputEmail2']
        password_doctor = request.POST['exampleInputPassword2']
        confirmation_doctor = request.POST['confirmation2']
        specs_doctor = request.POST['exampleInputSpeci1']
        hospitals = request.POST['Hospital']
        usernameDr = request.POST['usernameDr']
        dob = request.POST['exampleInputDate1']

        if password_doctor == confirmation_doctor:
            if DoctorInfo.objects.filter(usernameDr=usernameDr).exists():  # see if username exists basically
                messages.add_message(request, messages.INFO, 'name is taken')
                return redirect('/')

            else:

                doctor_person = DoctorInfo(firstname=firstName_doctor,
                                           lastname=lastName_doctor,
                                           specialization=specs_doctor,
                                           confirmation=confirmation_doctor,
                                           password=password_doctor,
                                           emailDr=email_doctor,
                                           hospital=hospitals,
                                           usernameDr=usernameDr,
                                           dob=dob
                                           )
                doctor_person.save()
                # dictionary for initial data with
                # field names as keys
                context = {}

                # add the dictionary during initialization
                context["dataset"] = ConfirmedAppointment.objects.all()

                return render(request, 'doctorPage.html', context)

        else:
            messages.add_message(request, messages.INFO, 'passwords are not matching')

            return redirect('/')
    return render(request, 'doctorPage.html')


