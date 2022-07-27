from django import forms
from user.models import MessageModel

class MessageForm(forms.ModelForm):
    class Meta:
        model=MessageModel
        fields ="__all__"