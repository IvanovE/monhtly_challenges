from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404() # debug must be True


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "h1": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404() # debug must be True
