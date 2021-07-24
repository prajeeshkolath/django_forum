
from forum.models import Category
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from django.views.generic.edit import FormView

from . import models
from . import serializers
from .forms import ContactForm

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pass

class CategoryView(TemplateView):
    template_name = 'category.html'
    http_method_names = ['get', 'post', 'put', 'delete'] 

    def get(self, request, *args, **kwargs):
        return super(CategoryView, self).get(self.request, page_type='home', *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(self).get(self.request, page_type='home', *args, **kwargs)


class CategoryApiView(views.APIView):
    template_name = 'category.html'
    def get(self, request, **kwargs):
        print(f'request={request}')
        return Response([{'hi': 'hello'}])

    def post(self, request, **kwargs):
        print(f'request={request}')
        return Response([])


class ForumHomeView(ListView):
    template_name = 'forum_home.html'
    model = models.Category
    # def get(self, **kwargs):
    #     context = super(ListView, self).get_context_data(**kwargs)
    #     context['categories']

class ThreadListView(TemplateView):
    template_name = 'thread_list.html'

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        print(form.cleaned_data)
        return super().form_valid(form)

    # def post(self, request):
    #     print(f'request = {request}')
    
