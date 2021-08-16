from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "january"
    elif month == 'february':
        challenge_text = "february"
    elif month == "march":
        challenge_text = "march"
    else:
        return HttpResponseNotFound("Really???")
    return HttpResponse(challenge_text)
