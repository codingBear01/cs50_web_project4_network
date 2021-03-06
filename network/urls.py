from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts", views.posts, name="posts"),
    path("create", views.create, name="create"),
    path("postedit", views.postEdit, name="postEdit"),
    path("removePost/<int:post_id>", views.removePost, name="removePost"),
    path("removeComment/<int:comment_id>", views.removeComment, name="removeComment"),
    path("comment/<int:post_id>", views.comment, name="comment"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("postLike", views.postLike),
    path("commentLike", views.commentLike),
    path("following/<str:username>", views.following, name="following"),
]
