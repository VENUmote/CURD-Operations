from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import col
from .forms import validate

def hello_world(request):
    dat={    
        'title':'venu',
        'ata':'Im here there were asre you from actually',
        'venu':['python','java','c'],
        'number':[10,20,30,40,50],
        'student':[
            {'name':'venu', 'mobile': 9398960491},
            {'name': 'narsaiah', 'mobile': 9652948249}

        ]
    }
    return render(request,'index.html',dat)
def venu(request):
    if request.method == 'POST':
        form = validate(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('view')
    else:
        form = validate() 
        return render(request, 'form.html', {'form' : form})

def view(request):
    cols = col.objects.all()
    print(cols)
    return render(request,'list.html', {'cols':cols})

def create(request):
    if request.method == 'POST':
        form = validate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = validate()
        return render(request, 'form.html',{'form':form , 'title': 'Add New Student'})


def edit(request,pk):
    student = get_object_or_404(col, pk=pk)
    if request.method == 'POST':
        form = validate(request.POST,instance=student)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        
        form = validate(instance=student)
        return render(request, 'form.html',{'form': form, 'title': 'Edit Student'})

def delete(request, pk):
    student = get_object_or_404(col, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('view')
    return render(request, 'delete.html', {'student': student})

