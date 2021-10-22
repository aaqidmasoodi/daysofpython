from django.shortcuts import render
from blog.models import Catagory, Post
# Create your views here.


def home_view(request):
    featured_posts_queryset= Post.objects.select_related('author').filter(featured=True)
    latest_posts_queryset = Post.objects.order_by('-date_posted')[:3]

    context = {
        'featured_posts': featured_posts_queryset,
        'latest_posts': latest_posts_queryset,

    }
    return render(request, 'index.html', context)