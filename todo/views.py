import datetime as dt

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm, CreateUserForm
from django.views.generic.edit import UpdateView

def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)

			return redirect('login')

	context = {'form':form}
	return render(request, 'todo/register.html', context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'todo/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def index(request):
    todo_list = Todo.objects.order_by('id').filter(user= request.user) # filtr zobrazí jen tásky, co dělal daný uživatel

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form, 'user' : request.user} # parametr user předá aktuálně přihlášeného uživatele, aby se zobrazili jen tásky od něho

    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        date = dt.date.fromisoformat(request.POST['date'])
        time = dt.time.fromisoformat(request.POST['time'])

        # date = dt.date(request.POST['date'])
        # time = dt.time(request.POST['time']) create_

        new_todo = Todo(text=request.POST['text'],date= dt.datetime.combine(date, time), user= request.user) # nový tásk bude mít sloupec user
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def uncompleteTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

class updateTask(UpdateView):
	model = Todo
	fields = ['text', 'complete', 'date']
	success_url = reverse_lazy('index')
	template_name = 'todo/update_task.html'
	# 	todo = Todo.objects.get(id=todo_id)
	#
	# 	form = TodoForm()
	#
	# 	if request.method == 'POST':
	# 		form = TodoForm(request.POST)
	# 		if form.is_valid():
	# 		form.save()
	# 		return redirect('index')
	#
	# context = {'form': form}
	# return render(request, 'todo/update_task.html', context)