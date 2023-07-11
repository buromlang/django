from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from views_code.models import Question
from django.http import Http404
from django.views.generic.base import TemplateView, RedirectView
from views_code.models import Question, Article, Manufacturer
from datetime import date
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import FormView
from views_code.forms import ContactForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, \
    TodayArchiveView


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><h3> It is now  </h3> <h1> %s </h1></html>" % now

    # return HttpResponseNotFound("<h1> url not found</h1>")
    return HttpResponse(html, status=201)


def question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("not found")
    return render(request, "polls/detail.html", {'question': question})


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello world')


class HomePageView(TemplateView):
    template_name = 'relations/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Question.objects.all()[:5]

        return context


class RedirectMethod(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'question-detail'

    def get_redirect_url(self, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        return super().get_redirect_url(*args, **kwargs)


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today_date'] = timezone.now()
        return context


class ArticleListView(ListView):
    model = Article
    paginate_by = 5

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*kwargs)
    #     context['today_date'] = timezone.now()
    #     return context


# class ContactFormView(FormView):
#     template_name = "views_code/form_template.html"
#     contact_class = ContactForm
#     success_url = "/thanks"


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "views_code/form_template.html"
    success_url = "/views_code/go-to-django/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = ['manufacturer_name']


class ManufacturerDetailView(DetailView):
    model = Manufacturer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = ['manufacturer_name']
    # suffix is optional
    template_name_suffix = "_update_form"


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    success_url = reverse_lazy('manufacturer-list')


class ManufactureListView(ListView):
    model = Manufacturer


class ArticleYearArchiveView(YearArchiveView):
    make_object_list = True
    allow_future = True
    queryset = Article.objects.all()
    date_field = 'pub_date'


class ArticleMonthArchiveView(MonthArchiveView):
    allow_future = True
    queryset = Article.objects.all()
    date_field = 'pub_date'


# class ArticleWeekArchiveView(WeekArchiveView):
#     queryset = Article.objects.all()
#     week_format = '%W'
#     date_field = 'pub_date'
#     allow_future = True


class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    print(queryset)
    date_field = "pub_date"
    week_format = "%W"
    allow_future = True


class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_date'
    allow_future = True


# class ArticleTodayArchiveView(TodayArchiveView):
#     queryset = Article.objects.all()
#     date_field = 'pub_date'
#     allow_future = True


