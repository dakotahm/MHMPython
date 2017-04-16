from django import forms


class LoginForm(forms.Form):
    usernameText = forms.CharField(25)
    passwordText = forms.CharField(25)

    def is_valid(self):
        return True
3