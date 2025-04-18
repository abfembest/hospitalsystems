from django.shortcuts import render, HttpResponse,redirect
from .forms import PatientForm, AdmissionForm, WardForm, BedForm
from .models import Patient, Admission, Ward, Bed
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'templates/admin/base.html')

""" Nurses Views """
def nurses(request):
    return render(request,'nurses/nurses.html')

def register_patient(request):
    patients = Patient.objects.all().order_by('-date_registered')
    
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_patient')  # reload with new data
    else:
        form = PatientForm()
        
    return render(request, 'nurses/register_patient.html', {
        'form': form,
        'patients': patients
    })

def admission_discharge_view(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)

            if admission.status == 'Discharged' and not admission.discharge_date:
                admission.discharge_date = timezone.now()

            admission.save()
            messages.success(request, f"{admission.patient} record updated successfully.")
            return redirect('admission_discharge')
    else:
        form = AdmissionForm()

    admissions = Admission.objects.select_related('patient', 'ward', 'bed').order_by('-admission_date')

    context = {
        'form': form,
        'admissions': admissions,
    }
    return render(request, 'nurses/admission_discharge.html', context)

def bed_ward_management_view(request):
    ward_form = WardForm()
    bed_form = BedForm()

    if request.method == 'POST':
        if 'ward_submit' in request.POST:
            ward_form = WardForm(request.POST)
            if ward_form.is_valid():
                ward_form.save()
                return redirect('bed_ward_management')
        elif 'bed_submit' in request.POST:
            bed_form = BedForm(request.POST)
            if bed_form.is_valid():
                bed_form.save()
                return redirect('bed_ward_management')

    wards = Ward.objects.prefetch_related('beds').all()
    context = {
        'ward_form': ward_form,
        'bed_form': bed_form,
        'wards': wards
    }
    return render(request, 'nurses/bed_ward_management.html', context)
                          
def doctors(request):
    return render(request, 'doctors/base.html')
                          
def ae(request):     
    return render(request, 'ae/base.html')
                            
def laboratory(request):
    return render(request, 'laboratory/base.html')
                           
def pharmacy(request):
    return render(request, 'pharmacy/base.html')
def accounts(request):
    return render(request, 'accounts/base.html')

                     
def hr(request):
    return render(request, 'hr/base.html')
                            
def inventory(request):
    return render(request, 'inventory/base.html')