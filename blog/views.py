from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-mountain",
        "image": "prof.png",
        "author": "Luan",
        "date": date(2023, 2, 20),
        "title": "Mountain",
        "excerpt": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam consequuntur neque quos eius sint?",
        "content": """Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam consequuntur neque quos eius sint?
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam consequuntur neque quos eius sint?
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam consequuntur neque quos eius sint?
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam consequuntur neque quos eius sint? """
    },
    {
        "slug": "programming-is-fun",
        "image": "prof.png",
        "author": "Luan",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "prof.png",
        "author": "Luan",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

#helpers

def get_date(post):
    return post['date']


# Create your views here.
def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):



    return render(request, "blog/post-detail.html")