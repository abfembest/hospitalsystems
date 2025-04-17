# # app/forms.py
# from django import forms
# from .models import Patient

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'
#         widgets = {
#             'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
#             'gender': forms.Select(attrs={'class': 'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(PatientForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             if not isinstance(field.widget, forms.FileInput):
#                 field.widget.attrs.update({'class': 'form-control'})

from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 2
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'address' and not isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control form-control-sm'})
