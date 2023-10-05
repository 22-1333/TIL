from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=30, required=False, help_text="30 characters or fewer.")
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('nickname',)