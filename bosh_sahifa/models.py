from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Publish"))

class Category(models.Model):
    nomi = models.CharField(max_length=30)
    #parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
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
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", default=True
    )
    tekst = RichTextField('matni')
    vaqt = models.DateTimeField(verbose_name='vaqti', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    rasm = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'
        ordering = ['-vaqt']

    def __str__(self):
         return self.mavzu

    def get_absolute_url(self):
        return reverse('oneOfNews', kwargs={"slug": str(self.slug)})

   # def get_absolute_url(self):
    #    return f'/news/{self.id}'


# commentlar qismi

class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


















































