from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Zero Eating Out.",
    "february": "Track Your Spending.",
    "march": "Try a No-Spend Month",
    "april": "No Retail Shopping.",
    "may": "Pay In Cash Only.",
    "june": "Avoid Social Media While Working.",
    "july": "Meal Prep Your Lunch.",
    "august": "Make One New Connection a Week.",
    "september": "Make One New Connection a Week",
    "october": "Work Breaks into Your Daily Routine",
    "november": "Read a Chapter of a Book a Day",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
