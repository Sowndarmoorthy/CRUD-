from django.shortcuts import render,redirect,get_object_or_404
from .models import Member

def index(request):
    mem = Member.objects.all()
    return render(request,"index.html",{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']

    mem = Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request, id):
    member = get_object_or_404(Member, id=id) 
    
    member.delete()
    return redirect("/",)

def update(request,id):
    mem = Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem = Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")