from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('n/home', views.nurses, name='nurse'),

    path('admission', views.admission_discharge_view, name='admission_discharge'),
    path('bed-ward-management', views.bed_ward_management_view, name='bed_ward_management'),
    path('vitals', views.vitals, name='vitals'),
    path('nursing_notes', views.nursing_notes, name='nursing_notes'),
    path('mar', views.mar, name='mar'),
    path('handover_logs', views.handover_logs_view, name='handover_logs'),
    path('task_assignments', views.task_assignments_view, name='task_assignments'),
    path('emergency_alerts', views.emergency_alerts_view, name='emergency_alerts'),

    path('d/home', views.doctors, name='doctors'),
    path('d/consultations', views.doctor_consultation, name='doctor_consultation'),
    path('d/medical-records/', views.access_medical_records, name='access_medical_records'),
    path('d/monitoring/', views.monitoring, name='monitoring'),

    path('ae/', views.ae, name='ae'),

    path('l/home', views.laboratory, name='laboratory'),
    path('l/test_entry', views.lab_test_entry, name='lab_test_entry'),
    path('l/upload_result', views.lab_result_upload, name='lab_result_upload'),
    path('l/internal_logs', views.lab_internal_logs, name='lab_internal_logs'),

    path('p/home', views.pharmacy, name='pharmacy'),
    path('p/review', views.review_prescriptions, name='review_prescriptions'),
    path('p/medication', views.dispense_medications, name='dispense_medications'),
    path('p/inventory', views.manage_inventory, name='manage_inventory'),
    path('p/reorder_alerts', views.reorder_alerts, name='reorder_alerts'),

    path('a/home', views.accounts, name='accounts'),
    path('a/payment_tracker', views.patient_payment_tracker, name='patient_payment_tracker'),
    path('a/financials', views.institution_financials, name='institution_financials'),
    path('a/financial_reports', views.financial_reports, name='financial_reports'),
    path('a/budget_planning', views.budget_planning, name='budget_planning'),

    path('hr/home', views.hr, name='hr'),
    path('hr/staff_profile', views.staff_profiles, name='staff_profiles'),
    path('hr/staff_attendance', views.staff_attendance, name='staff_attendance_shift'),
    path('hr/staff_transitions', views.staff_transitions, name='staff_transitions'),
    path('hr/staff_certifications', views.staff_certifications, name='staff_certifications'),

    path('inventory/', views.inventory, name='inventory'),

    path('ad/home', views.hms_admin, name='hms_admin'),
    path('ad/operations', views.director_operations, name='director_operations'),
    path('ad/reports', views.director_reports, name='director_reports'),
    path('ad/accounts', views.user_accounts, name='user_accounts'),

    path('r/home', views.receptionist, name='receptionist'),
    path('r/new_patient', views.register_patient, name='register_patient'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
