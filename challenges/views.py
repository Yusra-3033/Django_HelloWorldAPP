from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges= {
    "january":"Quit the shit get fit!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn a new skill!",
    "april": "loose weight!",
    "may":"Study for exams!",
    "june":"Read 3 books!",
    "july":"Quit the shit get fit!",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn a new skill!",
    "oktober": "loose weight!",
    "november":"Study for exams!",
    "december":None,
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    #for month in months:
        #capitalized_month = month.capitalize()
       # month_path = reverse("month-challenge", args=[month])
       # list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This is not a month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request,"challenges/challenge.html", {"month":month , "text":challenge_text})
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        #raise Http404()