from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import timedelta, datetime


@login_required(login_url="login")
def home(request):
    issues = models.SocialIssue.objects.all().order_by("-submit_date")
    page = request.GET.get("page", 1)
    paginator = Paginator(issues, 5)
    total_cnt = issues.count()
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
    user = request.user
    d = {"issues": issues, "user": user}
    return render(request, "main/home.html", d)


@login_required(login_url="login")
def create_issue(request):
    form = forms.SocialIssueForm
    if request.method == "POST":
        form = forms.SocialIssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            messages.success(request, "Thank you for contributinh to the society")
            return redirect("home")
    d = {"form": form}
    return render(request, "main/create_issue.html", d)


@login_required(login_url="login")
def filter_issue(request):
    try:
        search = request.GET["search"]
    except:
        search = ""
    if search:
        issues = models.SocialIssue.objects.filter(title__icontains=search)
        length = len(issues)
    else:
        issues = models.SocialIssue.objects.all()
        length = len(issues)
    d = {"issues": issues, "length": length}
    return render(request, "main/filter_issues.html", d)


@login_required(login_url="login")
def recent_issues(request):
    issues = models.SocialIssue.objects.filter(
        submit_date__gt=datetime.today() - timedelta(30)
    ).distinct()
    d = {"issues": issues}
    return render(request, "main/recent.html", d)


@login_required(login_url="login")
def trending_issues(request):
    issues = models.SocialIssue.objects.filter(comments__gt=3).distinct()
    d = {"issues": issues}
    return render(request, "main/trending.html", d)


@login_required(login_url="login")
def particular_issue(request, pk):
    issue = get_object_or_404(models.SocialIssue, pk=pk)
    comments = models.SocialIssueComments.objects.filter(social_issue=issue).order_by(
        "-submit_date"
    )
    if request.method == "POST":
        comment = request.POST["comment"]
        obj = models.SocialIssueComments.objects.create(
            comment=comment, social_issue=issue, user=request.user
        )
        obj.save()
        messages.success(request, "Thanks for commenting on issue")
    d = {"issue": issue, "comments": comments}
    return render(request, "main/particular_issue.html", d)


@login_required(login_url="login")
def my_issues(request):
    issues = models.SocialIssue.objects.filter(user=request.user)
    d = {"issues": issues}
    return render(request, "main/my_issues.html", d)
