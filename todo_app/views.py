from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from todo_app.forms import TodoForm, FormName
from todo_app.models import Todo, Name


def index(request):
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            form_name = Name(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                text=form.cleaned_data['text']
            )
            form_name.save()
        # else:
        #     form = FormName(request.POST)
        #     context = {
        #         'form': form
        #     }
        #     return render(request, 'todo_app/index.html', context)

        return redirect('all_todos')

    else:
        form_name = FormName()
        context = {
            'form_name': form_name
        }
        return render(request, 'todo_app/index.html', context)


def todos_all(request):
    if request.method == 'GET':
        context = {
            'todos': Todo.objects.all()
        }
        return render(request, 'todo_app/todos.html', context)


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                is_done=False)
            todo.save()
            return redirect('all_todos')
    else:
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo_app/create.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.save()
            return redirect('all_todos')
    form = TodoForm(initial=todo.__dict__)
    return render(request, 'todo_app/create.html', {'form': form})


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.delete()
            return redirect('all_todos')

    form = TodoForm(initial=todo.__dict__)
    return render(request, 'todo_app/create.html', {'form': form})
