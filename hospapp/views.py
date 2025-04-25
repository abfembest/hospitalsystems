from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Patient, Admission, Ward, Bed, HandoverLog, TaskAssignment, Shift, EmergencyAlert
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse,redirect
from .forms import PatientForm, AdmissionForm, WardForm, BedForm

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
                          
def vitals(request):
    return render(request, 'nurses/vital_signs.html')

def nursing_notes(request):
    return render(request, 'nurses/nursing_notes.html')

def mar(request):
    return render(request, 'nurses/mar.html')

# @login_required
def handover_logs_view(request):
    if request.method == 'POST' and 'handover_submit' in request.POST:
        patient_id = request.POST.get('patient_id')
        notes = request.POST.get('notes')

        if patient_id and notes:
            try:
                patient = Patient.objects.get(id=patient_id)
                HandoverLog.objects.create(
                    patient=patient,
                    author=request.user,
                    notes=notes
                )
            except Patient.DoesNotExist:
                # optionally handle error if patient is not found
                pass

        return redirect('handover_logs')  # update with your actual URL name

    context = {
        'patients': Patient.objects.all(),
        'handovers': HandoverLog.objects.select_related('patient', 'author').order_by('-timestamp')[:50],
    }
    return render(request, 'nurses/handover_logs.html', context)

def task_assignments_view(request):
    if request.method == 'POST':
        nurse_id = request.POST.get('nurse_id')
        shift_id = request.POST.get('shift_id')
        task_description = request.POST.get('task_description')

        if nurse_id and shift_id and task_description:
            nurse = User.objects.get(id=nurse_id)
            shift = Shift.objects.get(id=shift_id)

            TaskAssignment.objects.create(
                nurse=nurse,
                shift=shift,
                task_description=task_description
            )
            return redirect('task_assignments')

    context = {
        'assignments': TaskAssignment.objects.select_related('nurse', 'shift').order_by('-created_at')[:50],
        'nurses': User.objects.all(),
        'shifts': Shift.objects.all()
    }
    return render(request, 'nurses/task_assignments.html', context)

def emergency_alerts_view(request):
    if request.method == 'POST':
        if 'acknowledge' in request.POST:
            alert_id = request.POST.get('alert_id')
            alert = EmergencyAlert.objects.get(id=alert_id)
            alert.acknowledged_by.add(request.user)

        elif 'trigger' in request.POST:
            message = request.POST.get('message')
            if message:
                EmergencyAlert.objects.create(
                    message=message,
                    triggered_by=request.user
                )
        return redirect('emergency_alerts')

    context = {
        'alerts': EmergencyAlert.objects.prefetch_related('acknowledged_by').order_by('-timestamp')[:50]
    }
    return render(request, 'nurses/emergency_alerts.html', context)

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

def hms_admin(request):
    return render(request, 'hms_admin/base.html')