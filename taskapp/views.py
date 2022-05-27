from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import  TaskModelForm,TaskUpdateForm
# Create your views here.

def index(request):

    #taking a post method from front end and processing them
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        #Handles the form and controlled from the front end
        form =  TaskModelForm()  

    # Takes data from the backend and makes it visible at the front end
      #ORM
    data = TaskModel.objects.all().order_by('-date')
    total_data = data.count()
    complete_task = TaskModel.objects.filter(isComplete=True).count()
    uncompleted_task = total_data - complete_task

    #passes data in the form of dictionaty(key:value) pair
    context = {
        'data': data,
        'form': form,
        'total_data':total_data,
        'complete_task' : complete_task,
        'uncompleted_task' : uncompleted_task,
    }
    # picks url from the user and returns it back to the user through frontend
    return render(request,'taskapp/index.html',context) 


#delete function
def delete(request,pk): 
    #accessing the data from database
    item = TaskModel.objects.get(id=pk)

    #accessing data from delete page
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'taskapp/delete.html')

#edit function
def edit(request,pk): 
    #accessing the data from database
    item = TaskModel.objects.get(id=pk)
    if request.method == "POST": 
        form = TaskUpdateForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        form = TaskUpdateForm(instance=item)

    context = {
        'form': form, 
    }
    return render(request,'taskapp/edit.html',context)

#this is the view from the route to the about page
def about(request):
    return render(request,'taskapp/about.html') 
    