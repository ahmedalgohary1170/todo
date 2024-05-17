from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.
def todolist(request):
    todolist = Todo.objects.filter(user=request.user)
    if request.method == 'POST':
        form =TodoForm(request.POST)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/list')
    else:
        form = TodoForm()

    return render(request,'todo/todo.html',{'object_list':todolist,'form':form})



def tododatial(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    change_status = request.GET.get('change_status','')
    if change_status:
        todo.completed =True
        todo.save()
        return redirect('/list')
    

    return render(request,'todo/todo_datail.html',{'todo_datial':todo})





















