from django import forms
from relations.models import Student


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100, widget=forms.TextInput)
    age = forms.IntegerField()
    # don't have TextField, PositiveIntegerField
    details = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def clean(self):
        print("clean method is called ")
        cleaned_data = self.cleaned_data
        print("cleaned data", cleaned_data)
        return cleaned_data


class ContactForm(forms.Form):
    template_name = "relations/form_template.html"
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        subject = cleaned_data.get('subject')

        if subject.lower().strip() == 'sales':
            print('error called ')
            self.add_error('subject', 'Sales emails are not allowed')
            # non field error appears before form starts
            raise forms.ValidationError('Sales emails are not allowed')

        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']

    template_name = 'relations/form_template.html'

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        name_in_db = Student.objects.filter(name__icontains=name)

        if name_in_db.exists():
            self.add_error('name', 'name already exist')

        return cleaned_data



