from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime
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
    post_list = Post.objects.filter(
        pub_date__lte=datetime(),
        is_published=True,
        category__is_published=True
    )[:4]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = get_object_or_404(
        Post.objects.select_related(
            'category'
        ).filter(
            is_published=True,
            category__is_published=True,
            category__slug=category_slug,
            pub_date__lte=datetime())
    )
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post_list = get_object_or_404(
        Post.objects.get(pk=id),
        (Q(pub_date__lte=datetime())
        | Q(is_published=True)
        | Q(category__is_published=True))
    )
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)
