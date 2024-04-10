from django.shortcuts import render

# Create your views here.

def generate(request):

    context = {
        "api_key": "sk-saMcB871NueeMnAO3SYpTwNiGRyz2D5t1rZtQBI9vfG56wF1"
    }

    return render(request, "image_apis/generate.html", context)