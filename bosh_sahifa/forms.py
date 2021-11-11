from captcha.fields import CaptchaField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, FileInput
from .models import News, Category, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['nomi']
        widgets = {'nomi': TextInput()}

class NewsForm(ModelForm):
    tekst = forms.CharField(widget=CKEditorUploadingWidget())
    #vaqt= DateTimeField(input_formats='%Y-%m-%d %I:%M %p')
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'mavzu': TextInput(attrs={'class': 'form-control'}),
            'rasm': FileInput(attrs={'class': 'input-image-control'}),
        }

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, widget=TextInput(attrs={'class': 'form-control'}), help_text='ixtiyoriy.')
    first_name = forms.CharField(max_length=30, required=False, widget=TextInput(attrs={'class': 'form-control'}), help_text='ixtiyoriy.')
    last_name = forms.CharField(max_length=30, required=False, widget=TextInput(attrs={'class': 'form-control'}),help_text='ixtiyoriy')
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}),help_text='soraladi')
    password1 = forms.CharField(max_length=30, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='parol')
    password2 = forms.CharField(max_length=30, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='parolni tasdiqlash')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ContactusForm(forms.Form):
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    captcha = CaptchaField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

class Loginform(forms.Form):
    username = forms.CharField(max_length=30, required=False, widget=TextInput(attrs={'class': 'form-control'}), help_text='foydalanuvchi nomi')
    password = forms.CharField(max_length=30, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='parol kiriting')
    def __init__(self, request, *args, **kwargs):
        # simply do not pass 'request' to the parent
        super().__init__(*args, **kwargs)
    class Meta:
        model = User
        fields = ('username', 'password2')


# kommentariya qismi

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")