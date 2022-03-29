from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Post, Comment


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def posts(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)

    posts = Post.objects.all()
    comments = Comment.objects.all()

    return render(
        request,
        "network/posts.html",
        {
            "posts": posts,
            "comments": comments,
        },
    )


def create(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)

        if request.method == "POST":
            postContent = request.POST.get("create_content").strip()

            if postContent == "":
                return render(
                    request,
                    "network/create.html",
                    {
                        "alertMessage": "You can't post with empty content!",
                    },
                )

            post = Post(
                user=user,
                content=postContent,
            )
            post.save()
            return redirect("posts")

        return render(request, "network/create.html")

    return render(request, "network/error.html")


def removePost(request, post_id):
    if request.method == "POST":
        if "post_delete" in request.POST:
            post = Post.objects.get(id=post_id)
            post.delete()
            return redirect("posts")
    return render(request, "network/posts.html")


def comment(request, post_id):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)

        if request.method == "POST":
            commentContent = request.POST.get("comment_content").strip()
            post = Post.objects.get(id=post_id)

            if commentContent == "":
                return render(
                    request,
                    "network/posts.html",
                    {
                        "alertMessage": "You can't comment with empty content!",
                    },
                )

            comment = Comment(
                user=user,
                post=post,
                content=commentContent,
            )
            comment.save()
            return redirect("posts")

    return render(request, "network/posts.html")


def profile(request):
    return render(request, "network/profile.html")


def following(request):
    return render(request, "network/following.html")
