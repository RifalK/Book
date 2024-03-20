from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import ModelForm
from RangerApp.models import Book, Category, Chat, Event, Mail, Salary, Service, Client, Setting
from django import forms


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('message', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'category', 'date', 'uploaded_by', 'desc')      


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
    


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'prix', 'description',)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('firt_name', 'last_name', 'society', 'email', 'address', 'contact', 'date', 'description',)



class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ('amount', 'date',)



class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('cname', 'pname', 'address', 'country', 'city', 'postal', 'email', 'number1', 'number2', 'number3', 'website',)

    

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date',)


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('email', 'user', 'subject', 'file', 'message',)