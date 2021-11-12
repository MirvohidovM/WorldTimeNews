from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DeleteView, UpdateView,ListView
from bosh_sahifa.forms import NewsForm, CommentForm
from bosh_sahifa.models import News


class YangilikViews(ListView):
    template_name = 'pages/yangiliklar.html'
    model = News
    context_object_name = 'news'
    paginate_by = 3
    def get_queryset(self):
        return News.objects.all().select_related('category')

def yangilikDetali(request, slug):
    template_name = "pages/oneOfNews.html"
    news = get_object_or_404(News, slug=slug)
    comments = news.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = news
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "news": news,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

class KategoriyaBoyicha(ListView):
    template_name = 'pages/yangiliklar.html'
    paginate_by = 3
    context_object_name = 'news'
    def get_queryset(self):
         return News.objects.filter(category_id=self.kwargs.get('pk')).select_related('category')

class YangilikAlmashtirish(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'pages/ozgartirish.html'
    form_class = NewsForm
    success_url = '/bosh-sahifa/news/'
    raise_exception = True


class YangilikTozalash(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'pages/tozalash.html'
    success_url = '/bosh-sahifa/news/'
    raise_exception = True

class YangilikYaratish(LoginRequiredMixin, CreateView):
    template_name = 'pages/qoshish.html'
    form_class = NewsForm
    success_url = '/bosh-sahifa/news/'
    raise_exception = True




# class YangilikDetali(DetailView):
#     model = News
#     template_name = 'pages/oneOfNews.html'
#     context_object_name = 'news'
#     def get_queryset(self):
#          return News.objects.filter(pk=self.kwargs.get('pk')).select_related('category')

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
#        news = News.objects.get(pk=news_id)
#        return render(request, 'pages/qoshish.html', {'news': news})