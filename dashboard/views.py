from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect("image_apis:generate")
    
    return render(request, "index.html")


def contactPage(request):
    return render(request, "contact.html")