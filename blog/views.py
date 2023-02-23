from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post


# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    stored_posts = request.session.get("stored_posts")
    if stored_posts is not None:
        is_saved_for_later  = post.id in stored_posts
    else:
        is_saved_for_later = False

    return render(request, "blog/post-detail.html",{
        "post": identified_post,
        "post_tags": identified_post.tags.all(),
        "saved_for_later": is_saved_for_later
    })

class ReadLaterView(View):    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts


        return HttpResponseRedirect("/")
    
