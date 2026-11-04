from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket


# =====================================
# USER REGISTRATION FORM
# =====================================

class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


# =====================================
# CREATE NEW SUPPORT TICKET FORM
# =====================================

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            'title',
            'description',
            'category',
            'priority'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter problem title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your IT problem'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


# =====================================
# UPDATE SUPPORT TICKET FORM
# =====================================

class TicketUpdateForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            'status',
            'priority'
        ]

        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
        }