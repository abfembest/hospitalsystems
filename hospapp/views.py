from django.shortcuts import render, HttpResponse,redirect
from .forms import PatientForm, AdmissionForm
from .models import Patient, Admission

# Create your views here.

def index(request):
    return render(request, 'templates/admin/base.html')

def nurses(request):
    return render(request,'nurses/nurses.html')
                          
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


# def register_patient(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST, request.FILES)  # include request.FILES
#         if form.is_valid():
#             form.save()
#             return redirect('patient_success')  # or to the list page
#     else:
#         form = PatientForm()
#     return render(request, 'nurses/register_patient.html', {'form': form})

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

            # Optional: Auto-set discharge date to now if status is "Discharged" and no date provided
            if admission.status == 'Discharged' and not admission.discharge_date:
                from django.utils import timezone
                admission.discharge_date = timezone.now()

            admission.save()
            messages.success(request, f"{admission.patient} record updated.")
            return redirect('admission_discharge')  # Update with your URL name
    else:
        form = AdmissionForm()

    admissions = Admission.objects.select_related('patient').order_by('-admission_date')

    context = {
        'form': form,
        'admissions': admissions
    }
    return render(request, 'nurses/admission_discharge.html', context)
                     
def hr(request):
    return render(request, 'hr/base.html')
                            
def inventory(request):
    return render(request, 'inventory/base.html')