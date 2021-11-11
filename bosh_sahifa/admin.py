from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from bosh_sahifa.models import News, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


class NewsAdminForm(forms.ModelForm):
    tekst = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


# class PostAdmin(SummernoteModelAdmin):
#     list_display = ("title", "slug", "status", "created_on")
#     list_filter = ("status", "created_on")
#     search_fields = ["title", "content"]
#     prepopulated_fields = {"slug": ("title",)}
#     summernote_fields = ("content",)

# kommentariya qismi
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# admin.site.register(Post, PostAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category)