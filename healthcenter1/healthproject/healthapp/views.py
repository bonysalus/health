from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Appointment, Department,DoctorList


# Create your views here.
def home(request):
    obj = Doctor.objects.all()
    return render(request, 'index.html', {'result': obj})


def news(request):
    return render(request, 'news.html')


def docdetail(request, doc_id):
    doctor = Doctor.objects.get(id=doc_id)
    return render(request, "docdetail.html", {'doctor': doctor})


def patient(request):
    doctor1 = DoctorList.objects.all()
    department1= Department.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        dep = request.POST['department']
        doc = request.POST['doctor']
        symptoms = request.POST['symptoms']
        message = request.POST['message']
        doctor = DoctorList.objects.filter(name=doc).first()
        department = Department.objects.filter(name=dep).first()

        try:
            Appointment.objects.create(name=name,email=email,date=date,symptoms=symptoms,
                                       message=message,doctor=doctor,department=department)


            return redirect('success')
        except:
            error = 'yes'

    return render(request, 'patient.html',{'doctor':doctor1 , 'department':department1})


def success(request):
    return render(request, 'success.html')

def allDocList(request,d_slug=None):
    d_page=None
    doctorlist=None
    if d_slug!=None:
        d_page=get_object_or_404(Department,slug=d_slug)
        doctorlist=DoctorList.objects.all().filter(department=d_page)
    else:
        doctorlist=DoctorList.objects.all().filter()
    return render(request,"department.html",{'department':d_page,'doctorlist':doctorlist})

def docDet(request,d_slug,doc_slug):
    try:
        doctorlist=DoctorList.objects.get(department__slug=d_slug,slug=doc_slug)
    except Exception as e:
        raise  e
    return render(request,'docdet.html',{'doctorlist':doctorlist})