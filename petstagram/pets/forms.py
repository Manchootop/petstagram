from django import forms
from django.core.exceptions import ValidationError

from petstagram.core.form_mixins import ReadOnlyFieldsFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['personal_photo'].label = 'Pet Photo:'

    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_photo')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            'name': 'Pet Name:',
            'personal_photo': 'Link to image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = ("date_of_birth",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['readonly'] = 'readonly'
        self._apply_readonly_on_fields()

    def clean_date_of_birth(self):
        # date_of_birth = self.cleaned_data['date_of_birth']
        # if date_of_birth != self.instance.date_of_birth:
        #     raise ValidationError('Date of birth is readonly.')
        #
        # return date_of_birth

        return self.instance.date_of_birth


class PetDeleteForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
