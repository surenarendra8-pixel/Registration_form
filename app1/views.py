import qrcode
import io
import base64

from django.shortcuts import render, redirect
from app1.models import Register
from app1.forms import Register_form

def qr_code_view(request):
    info = Register.objects.all()
    form = Register_form()
    url = "https://registration-form-z3vc.onrender.com/register/"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'home.html', {'info': info, 'form': form, 'qr_image': img_str})

def new_registration(request):
    info = Register.objects.all()
    form = Register_form()
    
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    
    return render(request, 'home.html', {'info': info, 'form': form})


def update_register(request, id):
    regis = Register.objects.get(id=id)
    form = Register_form(instance=regis)
    
    if request.method == 'POST':
        form = Register_form(request.POST, instance=regis)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    
    return render(request, 'update_form.html', {'form': form})