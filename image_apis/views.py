from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from account.models import User

import json

def decrease_tokens(request):
    data = json.loads(request.body)
    try:
        user = User.objects.get(id=data["userId"])
        user.token -= data["amount"]
        user.save()
    except User.DoesNotExist as e:
        return JsonResponse({"status": "error", "error": e.__str__})

    return JsonResponse({"status": "ok"})


@login_required
def generate(request):

    
    context = {
        "api_key": "sk-saMcB871NueeMnAO3SYpTwNiGRyz2D5t1rZtQBI9vfG56wF1",
        "userId": request.user.id,
        "userToken": request.user.token,
    }

    return render(request, "image_apis/generate.html", context)




