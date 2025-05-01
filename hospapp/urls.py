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
    # path('patient_list', views.patient_list, name='patient_list'),
    # path('doctors/patient-list/', views.patient_list, name='patient_list'),
    # path('doctor/view/<int:patient_id>/', views.view_patient, name='view_patient'),
    # path('doctor/diagnose/<int:patient_id>/', views.add_diagnosis, name='add_diagnosis'),
    # path('doctor/prescribe/<int:patient_id>/', views.prescribe_med, name='prescribe_med'),
    # path('doctor/notes/<int:patient_id>/', views.write_notes, name='write_notes'),

    path('ae/', views.ae, name='ae'),

    path('l/home', views.laboratory, name='laboratory'),
    path('l/test_entry', views.lab_test_entry, name='lab_test_entry'),
    path('l/upload_result', views.lab_result_upload, name='lab_result_upload'),
    path('l/internal_logs', views.lab_internal_logs, name='lab_internal_logs'),

    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('accounts/', views.accounts, name='accounts'),
    path('hr/', views.hr, name='hr_page'),
    path('inventory/', views.inventory, name='inventory'),
    path('hms_admin', views.hms_admin, name='hms_admin'),

    path('r/home', views.receptionist, name='receptionist'),
    path('r/new_patient', views.register_patient, name='register_patient'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
