from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts", views.posts, name="posts"),
    path("create", views.create, name="create"),
    path("removePost/<int:post_id>", views.removePost, name="removePost"),
    path("comment/<int:post_id>", views.comment, name="comment"),
    path("profile", views.profile, name="profile"),
    path("following", views.following, name="following"),
]
