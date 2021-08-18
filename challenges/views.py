from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "january1",
    "february": "february1",
    "march": "march1",
    "april": "april1",
    "may": "may1",
    "june": "june1",
    "july": "july1",
    "august": "august1",
    "september": "september1",
    "october": "october1",
    "november": "november1",
    "december": "december1"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    if 0 < month < 13:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_url = reverse("monthly-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound("Really???")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "h1": month
        })
    except:
        return HttpResponseNotFound("Really???")
