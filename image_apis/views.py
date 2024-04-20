from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from account.models import User

from .utils import generate_image

import json


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


@csrf_exempt
def generate_ajax(request):
    context = {}
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        user_id = request.POST.get("userId")
        response = generate_image(prompt)
        context["image"] = b'asd'

        """
        if response.status_code == 200:
            user = User.objects.get(id=user_id)
            user.token -= 1
            user.save()
            context["image"] = response.content
        else:
            context["error"] = str(response.json())
        """

    return HttpResponse(b'asdasd', content_type="image/png")
    return HttpResponse(response.content, content_type="image/png")