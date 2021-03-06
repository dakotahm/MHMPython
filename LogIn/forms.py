from django import forms
from LogIn import models
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    """
    Login form which accepts a username and password.
    
    Will be authenticated using Django's login authentication
    """
    username = forms.CharField(25)
    password = forms.CharField(25)

    def is_valid(self):
        return True


class RegistrationForm(forms.Form):
    """
    Registration form which accepts a username, password, and password confirmation.
    Email is unused for our application.
    
    Validated using regex, and will be authenticated using Django's UserCreationForm
    """
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("username"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("password"))

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))

    def clean_username(self):
        """
        Checks to see is username has already been registered
        
        :return: 
        """
        try:
            user = models.AuthUser.objects.get(username__iexact=self.cleaned_data['username'])
        except models.AuthUser.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        """
        Checks to see if password and password confirmation match
        
        :return: 
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
