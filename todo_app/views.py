from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from todo_app.forms import TodoForm, FormName
from todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,

    }
    return render(request, 'todo_app/index.html', context=context)


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                is_done=False)
            todo.save()
            return redirect('todos index')
    else:
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo_app/create.html', context)


def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'GET':
        form=TodoForm


def delete(request, todo_id):
    pass
