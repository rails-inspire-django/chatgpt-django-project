from django import forms
from django.core.validators import MinLengthValidator

from .models import Chat, Message


class MessageForm(forms.ModelForm):
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'class': "rounded-lg border-gray-300 block leading-normal border px-4 text-gray-700 bg-white "
                         "focus:outline-none py-2 appearance-none w-full",
                'data-controller': "textarea-autogrow",
                "placeholder": "Ctrl + Enter to send",
            },
        ),
        validators=[MinLengthValidator(2)]
    )

    class Meta:
        model = Message
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        self.role = kwargs.pop("role")
        self.chat_pk = kwargs.pop("chat_pk")

        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.chat_id = self.chat_pk
        instance.role = self.role
        if commit:
            instance.save()
        return instance
