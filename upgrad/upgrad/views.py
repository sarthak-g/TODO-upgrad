from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
def index(request):
    HttpResponse('HELLO')
    return render(request,'index.html')
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
