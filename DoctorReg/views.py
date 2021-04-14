from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from DoctorReg.models import DoctorInfo

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
        dob_doctor = request.POST['exampleInputDate1']

        if password_doctor == confirmation_doctor:
            if DoctorInfo.objects.filter(firstname=firstName_doctor).exists(): #see if username exists basically
                messages.add_message(request, messages.INFO, 'name is taken')
                return redirect('/')

            else:

                doctor_person = DoctorInfo(firstname=firstName_doctor,
                                           lastname=lastName_doctor,
                                           dob=dob_doctor,
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
