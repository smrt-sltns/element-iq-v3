from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from account.models import User

from account.auth import admin_only
from .utils import generate_image

import json
import base64


@csrf_exempt
def decrease_tokens(request):
    if request.method != "POST":
        return JsonResponse({"error": "method not allowed"})
    user_id = request.POST.get("userId")
    token_used = request.POST.get("amount")
    try:
        user = User.objects.get(id=user_id)
        user.token -= int(token_used)
        user.save()
    except User.DoesNotExist as e:
        return JsonResponse({"status": "error", "error": e.__str__})

    return JsonResponse({"status": "ok", "remainingTokens": user.token})

@login_required
@admin_only
def generate(request):

    context = {
        "api_key": "sk-saMcB871NueeMnAO3SYpTwNiGRyz2D5t1rZtQBI9vfG56wF1",
        "userId": request.user.id,
        "userToken": request.user.token,
    }

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        response = generate_image(prompt)
        if response.status_code == 200:
            context["image"] = response.content
        else:
            context["error"] = str(response.json())
    

    return render(request, "image_apis/generate.html", context)

@login_required
def admin_restriction(request):
    data = "You need to be a superuser to access this feature"
    
    # Create an HTTP response with the data
    response = HttpResponse(data)
    
    # Optionally, you can set headers, status codes, content types, etc.
    response['Custom-Header'] = 'Some value'
    response.status_code = 200  # Default status code is 200 (OK)
    response['Content-Type'] = 'text/plain'  # Set the content type
    
    return response


@csrf_exempt
def generate_ajax(request):
    context = {}

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        user_id = request.POST.get("userId")
        response = generate_image(prompt)
        if response.status_code == 200:
            user = User.objects.get(id=user_id)
            user.token -= 1
            user.save()
            context["userToken"] = user.token
            image_data = base64.b64encode(response.content).decode('utf-8')
            context["image"] = image_data
        else:
            context["error"] = str(response.json())
    
    return JsonResponse(
        context
    )
    # return HttpResponse(response.content, content_type="image/png")
