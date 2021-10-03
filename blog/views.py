from django.shortcuts import render, get_object_or_404
from . import models


def posts(request):
    posts = models.Post.objects.filter(published_at__isnull=False).order_by(
        "-published_at"
    )
    return render(request, "blog/posts.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(models.Post, id=id)
    return render(request, "blog/post_detail.html", {"post": post})
