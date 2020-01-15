from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                user = authenticate(username=username, password=password)

                if not user:
                    raise forms.ValidationError("Usuário não encontrado")
                elif not user.check_password(password):
                    raise forms.ValidationError("Senha incorreta")
                elif not user.is_active:
                    raise forms.ValidationError("Usuário desativado")
            except Exception as e:
                print(e)

            return super(LoginForm, self).clean()
        raise forms.ValidationError("Usuário e senha inválidos")