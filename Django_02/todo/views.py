from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo

# Create your views here.
# 목록 화면 뷰
def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html',{'todos':todos})

# 상세 조회 뷰
def todo_detail (request,pk):
    todo = Todo.objects.get(id=pk)
    return render (request, 'todo/todo_detail.html', {'todo':todo})

# 생성 뷰
def todo_post(request):
    if request.method == "POST":    # POST 요청이 들어오는 경우
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:  # GET 요청이 들어오는 경우
        form = TodoForm()
    return render(request,'todo/todo_post.html',{'form':form})

# 수정 뷰
def todo_edit(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request,'todo/todo_edit.html',{'form':form})

# 완료 목록 뷰
def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html',{'dones':dones})

# 완료로 바꾸는 뷰
def todo_done(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')