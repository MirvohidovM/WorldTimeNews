from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    nomi = models.CharField(max_length=30)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategoriyalar'

    def get_absolute_url(self):
        return reverse('kategoriya', kwargs={'pk':self.pk})

    #def get_absolute_url(self):
       # return f'/category/{self.id}'

    def __str__(self):
        return self.nomi

class News(models.Model):
    mavzu = models.CharField('mavzusi', max_length=150)
    tekst = RichTextField('matni')
    vaqt = models.DateTimeField(verbose_name='vaqti', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='images', blank=True)
    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'
        ordering = ['-vaqt']

    def __str__(self):
         return self.mavzu

    def get_absolute_url(self):
        return reverse('oneOfNews', kwargs={'pk':self.pk})

   # def get_absolute_url(self):
    #    return f'/news/{self.id}'