from django import forms
from django.forms import ModelForm, ValidationError
from .models import Report, User

class InputForm(forms.Form):
    url = forms.URLField(max_length=250, help_text='URLni kiriting')

# class ReportForm(forms.Form):
#     shorturl = forms.URLField(max_length=60, help_text="URLni kiriting")
#     textarea = forms.CharField()
#     captcha = forms.IntegerField()
class ContactForm(forms.ModelForm):
    class Meta:
        model = User #models.User
        fields = ['name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data['email']
        if (len(email) == 0) or ('@' not in email) or ('.' not in email):
            raise forms.ValidationError("Emailingizni 'example@gmail.com' shaklida kiriting")
        return email
        # if User.objects.filter(email=email).exists():
        #     raise forms.ValidationError('Ushbu email sistemada ro\'yxatdan o\'tkazilgan.')
        # return email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # email = self.request.POST.get('email')
        print('email:', email)
        if (len(email) == 0) or ('@' not in email) or ('.' not in email):
            raise forms.ValidationError("Emailingizni 'example@gmail.com' shaklida kiriting")
        return email

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['shorturl', 'email', 'message']

    def clean_email(self):
        super(ReportForm, self).clean()
        email = self.cleaned_data.get('email')
        # email = self.request.POST.get('email')
        print('email:', email)
        if (len(email) == 0) or ('@' not in email) or ('.' not in email):
            raise forms.ValidationError("Emailingizni 'example@gmail.com' shaklida kiriting")
        return email


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=200, required=True)
#     email = forms.EmailField(max_length=120, required=True)
#     message = forms.CharField(max_length=1000 ,required=True)
    
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         print(email)
#         if len(email) == 0 or ('@' not in email):
#             raise forms.ValidationError("Email bosh bo'lishi mumkin emas")
#         return email
     