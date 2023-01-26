from django.shortcuts import render, redirect
from .models import Student, Blog


def loadhtml(request):
    data=Blog.objects.all
    return render(request, "home.html",{"data":data})


def signup(request):
    if request.session.has_key('is_login'):
        return redirect('/home')
    return render(request, "registration.html")


def savedata(request):
    if request.POST:
        sid = request.POST['sId']
        sname = request.POST['sName']
        semail = request.POST['sEmail']
        spassword = request.POST['sPassword']
        obj = Student(sId=sid, sName=sname, sPassword=spassword, sEmail=semail)
        obj.save()
    return redirect('/login')


def login(request):
    if request.session.has_key('is_login'):
        return redirect('/home')
    if request.POST:
        semail = request.POST['sEmail']
        spassword = request.POST['sPassword']
        count = Student.objects.filter(sEmail=semail, sPassword=spassword).count()
        if count > 0:
            request.session['is_login'] = True
            request.session['user_id'] = Student.objects.values('id').filter(sEmail=semail, sPassword=spassword)[0]['id']
            return redirect('/loadhtml')
        else:
            return redirect('/#')
    return render(request, "login.html")

def aboutus(request):
    return render(request,"aboutus.html")


def home(request):
    data = Blog.objects.all
    return render(request, "home.html", {"data": data})

def logout(request):
    del request.session['is_login']
    return redirect('/login')

def createpost(request):
    if request.POST:
        uid = request.POST['user_id']
        pname = request.POST['pname']
        ptitle = request.POST['ptitle']
        pdetail = request.POST['pdetail']
        img = request.FILES['img']
        obj = Blog(publisherName=pname,title=ptitle,postDetail=pdetail,image=img)
        obj.user_id_id = uid
        obj.save()
    return render(request,"createPost.html")

def services(request):
    return render(request,"services.html")

def company(request):
    return render(request,"company.html")

def sendemail(request):
    if request.POST:
        name = request.POST['name']
        mail = request.POST['mail']
        comment = request.POST['comment']
        obj = Blog(name=name,mail=mail,comment=comment)
        obj.save()
    return render(request,"sendemail.html")



