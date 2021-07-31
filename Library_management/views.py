from django.shortcuts import render
from Library_management.models import book
from django.contrib import messages
from django.db.models import Q

def bkdisplay(request):
    if 's' in request.GET:
        s=request.GET['s']
        results=book.objects.filter(Q(title__icontains=s) | Q(genre__icontains=s))

    else:
        results=book.objects.all()
    return render(request,"index.html",{"book":results})

def bkinsert(request):
    if request.method=="POST":
        if request.POST.get('title') and request.POST.get('author') and request.POST.get('genre') and request.POST.get('height') and request.POST.get('publisher'):
            savest=book()
            savest.title=request.POST.get('title')
            savest.author=request.POST.get('author')
            savest.genre=request.POST.get('genre')
            savest.height=request.POST.get('height')
            savest.publisher=request.POST.get('publisher')
            savest.save()

            messages.success(request,"The record "+savest.title+" Is saved successfully")
            return render(request,"Create.html")
    else:
            return render(request,"Create.html")
    
def bkdelete(request, id):
    delbook = book.objects.get(id=id)
    delbook.delete()
    results = book.objects.all()
    return render(request, "index.html", {"book":results})