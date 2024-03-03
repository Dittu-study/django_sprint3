from django.shortcuts import render
from django.http import Http404

def index(request):
    template = 'blog/index.html'
    context = {'posts': reversed(posts), 'full_post': True}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    if dict_posts.get(id) is None:
        raise Http404("list is empty")
    context = {'post': dict_posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'slug': category_slug}
    return render(request, template, context)
