from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login


class SignUpForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {"password": forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error("repeat_password", "Passwords must match")

        return cleaned_data

    def signup(self, request):
        self.cleaned_data.pop("repeat_password")
        return User.objects.create_user(**self.cleaned_data)

