from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    follower = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="user_follower",
    )
    following = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="user_following",
    )


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name="post_like")

    def __str__(self):
        return f"Author: {self.user} | Posted Time: {self.created_time} | Likes: {self.like.count()}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_author"
    )
    post = models.ForeignKey(
        Post,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comment_post",
    )
    content = models.TextField(max_length=300)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name="comment_like")

    def __str__(self):
        return f"Author: {self.user} | Commented Time: {self.created_time} | Likes: {self.like.count()}"
