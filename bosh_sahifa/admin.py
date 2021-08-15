from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from bosh_sahifa.models import News, Category

class NewsAdminForm(forms.ModelForm):
    tekst = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

admin.site.register(News, NewsAdmin)
admin.site.register(Category)