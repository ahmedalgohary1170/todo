from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
# from .forms import TodoForm
# Create your views here.
# def todolist(request):
#     todolist = Todo.objects.filter(user=request.user)
#     if request.method == 'POST':
#         form =TodoForm(request.POST)
#         if form.is_valid:
#             myform = form.save(commit=False)
#             myform.user = request.user
#             myform.save()
#             return redirect('/list')
#     else:
#         form = TodoForm()

#     return render(request,'todo/todo.html',{'object_list':todolist,'form':form})



# def tododatial(request,pk):
#     todo = get_object_or_404(Todo,pk=pk)
#     change_status = request.GET.get('change_status','')
#     if change_status:
#         todo.completed =True
#         todo.save()
#         return redirect('/list')
    

#     return render(request,'todo/todo_datail.html',{'todo_datial':todo})




###################################################################

def index(request):
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'todo/index.html', {'todos': todos})



# Creating a new Todo
def create_todo(request):
    title = request.POST.get('title')
    user = request.user
    
    todo = Todo.objects.create(title=title,user=user)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})

# Marking completed True
def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})

# Deleting a Todo
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})




















