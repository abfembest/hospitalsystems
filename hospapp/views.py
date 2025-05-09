from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, AdmissionForm, WardForm, BedForm
from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from .models import Patient, Admission, Ward, Bed, HandoverLog, TaskAssignment, Shift, EmergencyAlert, MedicalRecord

# Create your views here.
def index(request):
    return render(request, 'templates/admin/base.html')

""" Nurses Views """
def nurses(request):
    return render(request,'nurses/index.html')

def bed_ward_management_view(request):
    return render(request, 'nurses/bed_ward_management.html')
                          
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

""" Doctors Views"""
def doctors(request):
    return render(request, 'doctors/index.html')

def doctor_consultation(request):
    return render(request, 'doctors/consultation.html')

# def patient_list(request):
#     return render(request, 'doctors/patient_list.html')

# View for the Patient List Page
# def patient_list(request):
#     patients = Patient.objects.all()
#     inpatients = patients.filter(is_inpatient=True)
#     outpatients = patients.filter(is_inpatient=False)
#     critical_count = patients.filter(status="critical").count()

#     context = {
#         'patients': patients,
#         'inpatients': inpatients,
#         'outpatients': outpatients,
#         'critical_count': critical_count
#     }
#     return render(request, 'doctors/patient_list.html', context)

# # View for Viewing Patient Profile
# def view_patient(request, patient_id):
#     patient = get_object_or_404(Patient, id=patient_id)
#     return render(request, 'doctors/view_patient.html', {'patient': patient})

# # View for Adding Diagnosis
# def add_diagnosis(request, patient_id):
#     patient = get_object_or_404(Patient, id=patient_id)
#     if request.method == 'POST':
#         # Logic for adding diagnosis here
#         # You can add diagnosis to the patient
#         diagnosis = request.POST.get('diagnosis')
#         patient.diagnosis = diagnosis
#         patient.save()
#         return HttpResponseRedirect(reverse('view_patient', args=[patient.id]))
#     return render(request, 'doctors/add_diagnosis.html', {'patient': patient})

# # View for Prescribing Medication
# def prescribe_med(request, patient_id):
#     patient = get_object_or_404(Patient, id=patient_id)
#     if request.method == 'POST':
#         # Logic for prescribing medication here
#         medication = request.POST.get('medication')
#         # Assume you have a Medication model to save prescriptions
#         patient.medication = medication
#         patient.save()
#         return HttpResponseRedirect(reverse('view_patient', args=[patient.id]))
#     return render(request, 'doctors/prescribe_medication.html', {'patient': patient})

# # View for Writing Notes
# def write_notes(request, patient_id):
#     patient = get_object_or_404(Patient, id=patient_id)
#     if request.method == 'POST':
#         # Logic for adding notes here
#         notes = request.POST.get('notes')
#         patient.notes = notes
#         patient.save()
#         return HttpResponseRedirect(reverse('view_patient', args=[patient.id]))
#     return render(request, 'doctors/write_notes.html', {'patient': patient})

# @login_required
def access_medical_records(request):
    patients = Patient.objects.all()
    return render(request, 'doctors/access_medical_records.html', {
        'patients': patients
    })

def monitoring(request):
    return render(request, 'doctors/treatment_monitoring.html')
                          
def ae(request):     
    return render(request, 'ae/base.html')

# Lab views                            
def laboratory(request):
    return render(request, 'laboratory/index.html')

def lab_test_entry(request):
    return render(request, 'laboratory/test_entry.html')

def lab_result_upload(request):
    return render(request, 'laboratory/result_upload.html')

def lab_internal_logs(request):
    return render(request, 'laboratory/logs.html')

# Pharmacy Views                           
def pharmacy(request):
    return render(request, 'pharmacy/index.html')

def review_prescriptions(request):
    return render(request, 'pharmacy/prescriptions.html')

def dispense_medications(request):
    return render(request, 'pharmacy/medication.html')

def manage_inventory(request):
    return render(request, 'pharmacy/inventory.html')

def reorder_alerts(request):
    return render(request, 'pharmacy/alerts.html')

# Acoounts Views
def accounts(request):
    return render(request, 'accounts/index.html')

def patient_payment_tracker(request):
    return render(request, 'accounts/payment_tracker.html')

def institution_financials(request):
    return render(request, 'accounts/financials.html')

def financial_reports(request):
    return render(request, 'accounts/financial_reports.html')

def budget_planning(request):
    return render(request, 'accounts/planning.html')

# HR Views
def hr(request):
    return render(request, 'hr/index.html')

def staff_profiles(request):
    return render(request, 'hr/staff_profiles.html')

def staff_attendance(request):
    return render(request, 'hr/staff_attendance_shift.html')

def staff_transitions(request):
    return render(request, 'hr/staff_transitions.html')

def staff_certifications(request):
    return render(request, 'hr/certifications.html')
                            
def inventory(request):
    return render(request, 'inventory/base.html')

# HMS Admin Views
def hms_admin(request):
    return render(request, 'hms_admin/index.html')

def director_operations(request):
    return render(request, 'hms_admin/operations.html')

def director_reports(request):
    return render(request, 'hms_admin/reports.html')

def user_accounts(request):
    return render(request, 'hms_admin/user_accounts.html')

def receptionist(request):
    return render(request, 'receptionist/index.html')

def register_patient(request):
    patients = Patient.objects.all().order_by('-date_registered')
    
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_patient')  # reload with new data
    else:
        form = PatientForm()
        
    return render(request, 'receptionist/register.html', {
        'form': form,
        'patients': patients
    })