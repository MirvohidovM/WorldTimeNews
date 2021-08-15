from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from bosh_sahifa.forms import NewsForm
from bosh_sahifa.models import News

#def news_views(request):
 #   news=News.objects.all()
  #  return render(request, 'pages/yangiliklar.html', {'news':news})

#def get_category(request, category_id):
 #   news = News.objects.filter(pk=category_id)
  #  return render(request, 'pages/yangiliklar.html', {'news': news})

#def oneOfNews(request, news_id):
 #   news = News.objects.filter(pk=news_id)
  #  return render(request, 'pages/oneOfNews.html', {'news': news})

#   def get_cats(request, category_id):
  #      news = News.objects.filter(category_id=category_id)
   #     category = Category.objects.get(pk=category_id)
    #    return render(request, 'pages/qoshish.html', {'news': news, 'category': category})

# def get_newsID(request, news_id):
    #    news = News.objects.get(pk=news_id)
     #   return render(request, 'pages/qoshish.html', {'news': news})


class YangilikViews(ListView):
    template_name = 'pages/yangiliklar.html'
    model = News
    context_object_name = 'news'
    paginate_by = 3

class Get_name(LoginRequiredMixin, CreateView):
    template_name = 'pages/qoshish.html'
    form_class = NewsForm
    success_url = '/bosh-sahifa/news/'
    raise_exception = True



class YangilikDetali(DetailView):
    model = News
    template_name = 'pages/oneOfNews.html'
    context_object_name = 'news'

class KategoriyaDetali(ListView):
    template_name = 'pages/yangiliklar.html'
    paginate_by = 3
    context_object_name = 'news'
    def get_queryset(self):
         return News.objects.filter(category_id=self.kwargs.get('pk'))

class YangilikAlmashtirish(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'pages/ozgartirish.html'
    form_class = NewsForm
    success_url = '/bosh-sahifa/news/'
    raise_exception = True

class YangilikTozalash(DeleteView):
    model = News
    template_name = 'pages/tozalash.html'
    success_url = '/bosh-sahifa/news/'



