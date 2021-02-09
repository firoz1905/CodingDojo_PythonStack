from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Show
import datetime 

# Create your views here.
def shows(request):
    ### Home page with all the shows
    return render(request,'home.html',context={
        "shows":Show.objects.all()
    })
def reroute(request):
    return redirect("/shows")
def new(request):
    ## Routing to new Show form
    if request.method=="GET":
        return render(request,'newshow.html')

def create(request):   
    if request.method=="POST":
        print(request.POST)
        print("Adding a new show")
        if 'e_message' not in request.session:
            request.session['e_message']=[]
        for key,val in request.POST.items():
            if val is "":
                request.session['e_message'].append("Please Enter all the fields")
            else:
                new_show=Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],desc=request.POST['desc'])
                print(new_show.id)
                return redirect(f"/shows/{new_show.id}") 
def show(request,show_id):
    ### view show Info
    if request.method=="GET":
        print("i am in the Show info display")
        context={
            "this_show":Show.objects.get(id=show_id)
        }
        return render(request,'showinfo.html',context)    

def edit(request,show_id):
    ## Edit show Info
    if request.method=="GET":
        return render(request,'editshow.html',context={
            "this_show": Show.objects.get(id=show_id)
        })
    if request.method=="POST":
        print(request.POST)
        if 'e1_message' not in request.session:
            request.session['e1_message']=[]
        for key,val in request.POST.items():
            if val is "":
                request.session['e1.message'].append("Please Enter all the fields")
            else:
                print("I am editing the Show Information")
                Show.objects.filter(id=show_id).update(title=request.POST['new_title'],network=request.POST['new_network'],release_date=request.POST['new_release_date'],desc=request.POST['new_desc'])
                return redirect(f"/shows/{show_id}")
    return redirect(f"/shows/{show_id}/edit")

def delete(request,show_id):
    if request.method=="EDIT":
        print("I am here to delete the show")
        Show.objects.filter(id=show_id).delete()
        return redirect("/shows")




