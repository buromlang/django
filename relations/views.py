from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from relations.forms import NameForm, ContactForm, StudentForm
from django.urls import reverse
from django.core.mail import send_mail


def index(request):
	return HttpResponse("index")


def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid:
			name = form.cleaned_data['name']
			return HttpResponse('thank you!')
	else:
		form = NameForm()
	return render(request, 'relations/info.html', {'form': form})


def to_send_mail(request):
	form = ContactForm()
	# form = ContactForm(request.POST or None)
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['buromlangs@gmail.com']

			send_mail(subject, message, sender, cc_myself, recipients)

	return render(request, 'relations/contact.html', {'form': form})


def student_detail(request):
	form = StudentForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		student_object = form.save()
		name = form.cleaned_data['name']
		age = form.cleaned_data['age']

	return render(request, 'relations/info.html', {'form': form})

