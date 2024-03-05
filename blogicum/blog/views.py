from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post
from datetime import datetime
from django.db.models import Q

# def index(request):
#     template = 'blog/index.html'
#     context = {'posts': reversed(posts), 'full_post': True}
#     return render(request, template, context)


# def post_detail(request, id):
#     template = 'blog/detail.html'
#     if dict_posts.get(id) is None:
#         raise Http404("list is empty")
#     context = {'post': dict_posts[id]}
#     return render(request, template, context)


# def category_posts(request, category_slug):
#     template = 'blog/category.html'
#     context = {'slug': category_slug}
#     return render(request, template, context)


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = Post.objects.filter(
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True
    )[:4]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)


def category_posts(request):
    template = 'blog/category.html'
    ice_cream_list = get_object_or_404(
        Post.objects.select_related(
            'category'
        ).filter(
            is_published=True,
            pub_date__lte=datetime.datetime.now()),
        is_published=True
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    ice_cream_list = get_object_or_404(
        Post.objects.get(pk=pk),
        Q(pub_date__lte=datetime.datetime.now())
        | Q(is_published=True)
        | Q(category__is_published=True)

    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
