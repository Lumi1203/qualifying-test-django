import requests
import random
from functools import wraps
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from .models import TestResult, Question


def examiner_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied

        if request.user.role != "examiner" and not request.user.is_superuser:
            raise PermissionDenied

        return view_func(request, *args, **kwargs)
    return _wrapped_view


@login_required
def take_test(request):
    final_questions = []

    db_questions = list(Question.objects.all())
    random.shuffle(db_questions)

    for q in db_questions[:3]:
        final_questions.append({
            "text": q.text,
            "options": {
                "A": q.option_a,
                "B": q.option_b,
                "C": q.option_c,
                "D": q.option_d,
            },
            "correct": q.correct_answer.upper(),
        })

    api_needed = 5 - len(final_questions)

    if api_needed > 0:
        response = requests.get(
            f"https://opentdb.com/api.php?amount={api_needed}&type=multiple"
        )
        data = response.json()["results"]

        for item in data:
            options = item["incorrect_answers"] + [item["correct_answer"]]
            random.shuffle(options)

            letters = ["A", "B", "C", "D"]
            option_map = dict(zip(letters, options))
            correct_letter = next(
                k for k, v in option_map.items()
                if v == item["correct_answer"]
            )

            final_questions.append({
                "text": item["question"],
                "options": option_map,
                "correct": correct_letter,
            })

    random.shuffle(final_questions)

    return render(request, "taketest/take_test.html", {
        "questions": final_questions
    })


@login_required
def save_result(request):
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
    results = TestResult.objects.filter(
        user=request.user
    ).order_by("-date_taken")

    return render(request, "taketest/my_results.html", {
        "results": results
    })


@login_required
def test_instructions(request):
    return render(request, "taketest/instructions.html")


@login_required
@examiner_required
def question_bank(request):
    questions = Question.objects.all().select_related("examiner").order_by('-created_at')
    return render(request, "taketest/question_bank.html", {
        "questions": questions
    })


@login_required
@examiner_required
def add_question(request):
    if request.method == "POST":
        Question.objects.create(
            examiner=request.user,
            text=request.POST["text"],
            option_a=request.POST["option_a"],
            option_b=request.POST["option_b"],
            option_c=request.POST["option_c"],
            option_d=request.POST["option_d"],
            correct_answer=request.POST["correct_answer"]
        )

        messages.success(request, "Question added successfully.")
        return redirect("question_bank")

    return render(request, "taketest/add_question.html")



@login_required
@examiner_required
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if not (request.user.is_superuser or question.examiner == request.user):
        return HttpResponseForbidden("You cannot edit this question.")

    if request.method == "POST":
        question.text = request.POST["text"]
        question.option_a = request.POST["option_a"]
        question.option_b = request.POST["option_b"]
        question.option_c = request.POST["option_c"]
        question.option_d = request.POST["option_d"]
        question.correct_answer = request.POST["correct_answer"]
        question.save()

        messages.success(request, "Question updated successfully.")
        return redirect("question_bank")

    return render(request, "taketest/edit_question.html", {
        "question": question
    })




@login_required
@examiner_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if not (request.user.is_superuser or question.examiner == request.user):
        return HttpResponseForbidden("You cannot delete this question.")

    question.delete()
    messages.success(request, "Question deleted successfully.")
    return redirect("question_bank")


