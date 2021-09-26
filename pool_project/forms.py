from django import forms

from .models import Poll

class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question','option_one','option_two','option_three']