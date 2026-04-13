from django.shortcuts import render
from django.shortcuts import redirect

from app1.models import Register
from app1.forms import Register_form

def new_registration(request):
    info = Register.objects.all()
    form = Register_form()

    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    
    return render(request, 'home.html',{'info':info, 'form':form})

'update'

def update_register(request,id):
    regis = Register.objects.get(id=id)
    form = Register_form(instance=regis)

    if request.method=='POST':
        form = Register_form(request.POST, instance=regis)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    return render(request,'update_form.html',{'form':form})
        





