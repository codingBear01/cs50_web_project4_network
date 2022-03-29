from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    likeCount = models.IntegerField(default=0)
    status_like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} created post at {self.created_time}"


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

    def __str__(self):
        return (
            f"Author: {self.user} | Post ID: {self.post.id} | Time: {self.created_time}"
        )
