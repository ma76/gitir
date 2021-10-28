from django import forms
from django.core import validators

# Define User-Code-Form
class UserCodeForm(forms.Form):
    project_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter project_name','class':'form-control'}),
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='enter lese than 20 char'),
            validators.MinLengthValidator(6, 'enter grater than 6 char')
        ]
    )
    repository = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter repository', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(limit_value=70,
                                          message='enter lese than 70 char'),
            validators.MinLengthValidator(6, 'enter grater than 6 char')
        ]
    )

    file = forms.FileField(
        widget=forms.FileInput(attrs={'class':'form-control'}),
        validators = [
            validators.FileExtensionValidator(allowed_extensions=['.py'],
                                              message='So sorry just python-file is allowed !'),

        ]
    )





# class UserCodeForm(forms.ModelForm):
#     class Meta:
#         model = UserCode
#         fields = '__all__'