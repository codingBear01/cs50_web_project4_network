from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from .models import User, Post, Comment, Profile


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

    posts = Post.objects.all().order_by("-created_time")
    comments = Comment.objects.all().order_by("-created_time")

    return render(
        request,
        "network/posts.html",
        {
            "posts": posts,
            "comments": comments,
        },
    )


@login_required
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


@login_required
def removePost(request, post_id):
    if request.method == "POST":
        if "post_delete" in request.POST:
            post = Post.objects.get(id=post_id)
            post.delete()
            return redirect("posts")
    return render(request, "network/posts.html")


@login_required
def removeComment(request, comment_id):
    if request.method == "POST":
        if "comment_delete" in request.POST:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return redirect("posts")
    return render(request, "network/posts.html")


@login_required
def comment(request, post_id):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)

        if request.method == "POST":
            commentContent = request.POST.get("comment_content").strip()
            posts = Post.objects.all()
            comments = Comment.objects.all()
            post = Post.objects.get(id=post_id)

            if commentContent == "":
                return render(
                    request,
                    "network/posts.html",
                    {
                        "alertMessage": "You can't comment with empty content!",
                        "posts": posts,
                        "comments": comments,
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


@login_required
@csrf_exempt
def postLike(request):
    if request.method == "POST":
        postID = request.POST.get("postID")
        postIsLiked = request.POST.get("postIsLiked")

        try:
            post = Post.objects.get(id=postID)
            if postIsLiked == "no":
                post.like.add(request.user)
                postIsLiked = "yes"
            else:
                post.like.remove(request.user)
                postIsLiked = "no"
            post.save()

            return JsonResponse(
                {
                    "postLikeCount": post.like.count(),
                    "postIsLiked": postIsLiked,
                    "status": 201,
                },
                status=201,
            )
        except:
            return JsonResponse(
                {
                    "error": "Post not found",
                    "status": 404,
                },
                status=404,
            )

    return JsonResponse({}, status=400)


@login_required
@csrf_exempt
def commentLike(request):
    if request.method == "POST":
        commentID = request.POST.get("commentID")
        commentIsLiked = request.POST.get("commentIsLiked")

        try:
            comment = Comment.objects.get(id=commentID)
            if commentIsLiked == "no":
                comment.like.add(request.user)
                commentIsLiked = "yes"
            else:
                comment.like.remove(request.user)
                commentIsLiked = "no"
            comment.save()

            return JsonResponse(
                {
                    "commentLikeCount": comment.like.count(),
                    "commentIsLiked": commentIsLiked,
                    "status": 201,
                },
                status=201,
            )
        except:
            return JsonResponse(
                {
                    "error": "Post not found",
                    "status": 404,
                },
                status=404,
            )

    return JsonResponse({}, status=400)


def profile(request, username):
    if request.user.is_authenticated:
        pageUser = User.objects.get(username=username)
    else:
        return render(request, "network/login.html")

    posts = Post.objects.all().filter(user=pageUser).order_by("-created_time")
    comments = Comment.objects.all().order_by("-created_time")
    usersFollows = Profile.objects.all().filter(user=request.user)

    return render(
        request,
        "network/profile.html",
        {
            "posts": posts,
            "comments": comments,
            "usersFollows": usersFollows,
            "pageUser": pageUser,
        },
    )


@login_required
@csrf_exempt
def follow(request):
    if request.method == "POST":
        user = request.POST.get("user")
        action = request.POST.get("action")
        return render(
            request,
            "network/profile.html",
            {
                "test": user,
            },
        )
    return render(request, "network/profile.html")
