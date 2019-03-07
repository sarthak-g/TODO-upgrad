from django.shortcuts import redirect,render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import TodoItem

# Create your views here.

class TODOView(ListView):
    model = TodoItem
    template_name = 'home.html'
class TODOCreateView(CreateView):
    model = TodoItem
    template_name = 'todo_create.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
class TODOUpdateView(UpdateView):
    model = TodoItem
    template_name = 'todo_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
class TODODeleteView(DeleteView):
    model = TodoItem
    template_name = 'todo_delete.html'
    context_object_name = 'delTODO'
    success_url = reverse_lazy('home')
def CompleteTodo(request, todo_id):
    mytodo = TodoItem.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('home')
def DeleteTodo(request):
    TodoItem.objects.filter(complete__exact=True).delete()
    return redirect('home')
