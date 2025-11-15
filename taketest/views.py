import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TestResult


@login_required
def take_test(request):
    """
    Fetch questions from API and display them to user.
    """
    response = requests.get("https://opentdb.com/api.php?amount=5&type=multiple")
    data = response.json()
    questions = data["results"]

    # We will handle scoring with JS, but Django will save results.
    return render(request, "taketest/take_test.html", {"questions": questions})


@login_required
def save_result(request):
    """
    Saves the score sent by AJAX from the browser.
    """
    if request.method == "POST":
        score = int(request.POST.get("score"))
        total = int(request.POST.get("total"))

        TestResult.objects.create(
            user=request.user,
            score=score,
            total_questions=total
        )

        return render(request, "taketest/result.html", {
            "score": score,
            "total": total
        })

    return redirect("take_test")


@login_required
def my_results(request):
    """
    Shows a table with past test results.
    """
    results = TestResult.objects.filter(user=request.user).order_by("-date_taken")

    return render(request, "taketest/my_results.html", {"results": results})

@login_required
def test_instructions(request):
    return render(request, 'taketest/instructions.html')