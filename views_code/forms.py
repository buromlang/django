from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    email = forms.EmailField()

    # def send_email(self):
    #     pass

    def send_email(self):
        email = self.cleaned_data['email']
        subject = "test form"
        body = "hi all"
        sender = "buromlangs@gmail.com"
        recipient = [email]

        send_mail(subject, body, sender, recipient)
