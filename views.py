from website.posts.models import Post
from django.shortcuts import render_to_response

def homepage(request):
    latest_post_list = Post.objects.all()[:5]
    return render_to_response('homepage.html', {'latest_post_list': latest_post_list})
