from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseServerError
from .models import BlogPost, Book

def index(request):
    #return HttpResponse("This is my blogapp")
    a = Book.objects.all()
    return render(request, 'index.html', {'books' : a})
    # b = BlogPost.objects.all()
    # return render(request, 'posts/index.html', {'posts' : b})

# def detail(request, book_id):
#     return HttpResponse(book_id) # For now, this just prints the parameter.

# def post_detail(request, book_id):
#     a = Book.objects.get(id = book_id)
#     return render(request, 'details.html', {'book': a})

def post_det(request, post_id):
    # post = BlogPost.objects.get(id = post_id)
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'details.html', {'posts': post})

def error_404(request, exception):
    return HttpResponse('ERR:404 - page is not found', status = 404)