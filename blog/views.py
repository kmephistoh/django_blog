from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import * 


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def logout_view(request):
    logout(request)
    # Redirect to a success page.

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/blog/home')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            error_message='username or password were incorrect.'
            return render(request, 'login.html', {"error_message":error_message})
    else:
        return render(request, 'login.html')

def article_list(request):
    articles_list =  Article.objects.all()
    paginator = Paginator(articles_list, 5) # Show 5 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
        
    return render(request, 'article_list.html', 
        {"articles": articles}
        )

def count_like(request):
    # messages.success(request, 'Thank you!')
    messages.error(request, "Don't repeat voting" )
    return render(request, "index.html", 
        )



