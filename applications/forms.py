from django import forms
#from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import DateInput

class DateInput(forms.DateInput):
    input_type = 'date'


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, trial):
        return trial.name


class ApplicationForm(forms.ModelForm):
    protocol_number= forms.IntegerField()
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    ergo = forms.ModelChoiceField(queryset=Ergo.objects.all(),widget = forms.Select(attrs={
            'id': 'yliko','placeholder': 'Choose material:'})
    )

    trials = CustomMMCF(
        queryset=Trial.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={
                'id': 'trial'})
    )
    # ergo__dokimi = forms.ModelMultipleChoiceField(queryset=ergo.)




    class Meta():
        model = Application
        fields = ['protocol_number','customer','ergo','trials']

        labels = {
        'trials': 'Trials'
        }
        help_texts = {
            'status_list': '(Seperated by comma)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trials'].queryset = Trial.objects.none()

        if 'ergo' in self.data:
            try:
                yliko_id = int(self.data.get('ergo'))
                print(yliko_id)
                self.fields['trials'].queryset = Trial.objects.filter(yliko_id=yliko_id).order_by('name')
            except (ValueError, TypeError):
                print("Hellooooooo!")  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            print("Adamakos")
            self.fields['trials'].queryset = self.instance.ergo.trial_set.order_by('name')


class UpdateApplicationForm(forms.ModelForm):


    class Meta():
        model = Application
        fields = ['status','customer']

        labels = {
        'status': 'Application status'
        }
        help_texts = {
            'status_list': '(Seperated by comma)',
        }








class CustomerForm(forms.ModelForm):




    class Meta():
        model = Customer
        fields = '__all__'










        # widgets = {
        #     'date': DateInput(attrs={'type': 'date'}),
        #     'class': 'form-control datetimepicker-input',
        #     'data-target': '#datetimepicker1'
        #
        # }


        # labels = {
        # 'protocol_number' : 'Protocol number'
        #
        # }

    #
    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "Password mismatch. Please try again!"
    #         )
