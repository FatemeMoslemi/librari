from django.shortcuts import render
from django.views import generic
from . import models

class index(generic.TemplateView):
    template_name = 'lib/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = models.Book.objects.all().count()
        context['authors'] = models.Author.objects.all().count()
        context['genres'] = models.Genre.objects.all().count()

        return context


# class BookListView(generic.ListView):
#     model = models.Book
#     template_name =
#
