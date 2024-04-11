from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account.models import User

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

    return render(request, "image_apis/generate.html", context)




