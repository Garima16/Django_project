from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user doesn't exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):

    #email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
                'username',
                'password',
                'email',
        )


    """"
    def set_password(self, raw_password):

        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hsh)


    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists:
            raise forms.ValidationError("This email is already registered!")
        return email

"""


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput,
                                   help_text='Choose a password consisting of alphabets in upper and lower case,special character and number')
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       help_text='Type the same password as above')


