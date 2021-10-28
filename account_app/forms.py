from django import forms
from django.contrib.auth.models import User
from django.core import validators
# Define Login-Form
class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter UserName','class':'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password','class':'form-control'}),
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if not is_exists_user:
            raise forms.ValidationError('you have mistake username or password !')

        return user_name

# Define Register-Form
class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter UserName','class':'form-control'}),
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='enter lese than 20 char'),
            validators.MinLengthValidator(6, 'enter grater than 6 char')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Email','class':'form-control'}),
        validators=[
            validators.EmailValidator('enter correct email !')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password','class':'form-control'}),
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'confirm password ','class':'form-control'}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('this email was gotten !')

        # if len(email) > 20:
        #     raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 20 باشد')

        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('This user_name already gotten !')

        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('You did not have similar passwords !')

        return password
