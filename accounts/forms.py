from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        help_text="Enter a strong password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'srn', 'semester', 'branch']

    def clean_password(self):
        password = self.cleaned_data.get("password")
        validate_password(password)
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
