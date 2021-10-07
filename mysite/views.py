from django.core.mail import message
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from mysite.forms import UserCreationForm
from django.contrib import messages

# start add
from django.http import HttpResponse
from article.models import Article
# end

# Create your views here.
# 画面の表示


def index(request):
    objs = Article.objects.all()
    context = {
        'articles' : objs,
    }
    return render(request,'mysite/index.html',context)


def contact(request):
    context = {}

    from django.core.mail import send_mail
    import os
    subject = 'subject'
    message = 'message'
    email_from = os.environ['EMAIL_HOST_USER']
    email_to = [
        os.environ['EMAIL_HOST_USER'],
        ]
    send_mail(
        subject,message,email_from,email_to
    )

    return render(request, 'mysite/contact.html', context)

class Login(LoginView):
    template_name = 'mysite/login.html'


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            messages.success(request, 'Complete signup')
            return redirect('/')
    return render(request, 'mysite/login.html', context)
