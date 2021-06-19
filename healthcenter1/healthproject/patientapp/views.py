from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('patientapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                return redirect('patientapp:register')
            else:
                user = User.objects.create_user(first_name=first_name,email=email,username=username,password=password)
                user.save()
                return redirect('patientapp:login')
        else:
            messages.info(request,"passwords not matching")
            return redirect('patientapp:register')
        return redirect('patientapp:login')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('healthapp:patient')
        else:
            messages.info(request,"invalid login credentials")
            return redirect('patientapp:login')

    return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')