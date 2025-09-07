from django.shortcuts import render,redirect
from .models import Patient

def Patients(request):
    return render(request,"patient.html")

def PatientInsert(request):
    if request.method == 'POST':
        print("from submitteed")
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            contact=contact,
            address=address
        )
        print("form saved")
        return redirect('home')
    return render(request,'Patient.html')

