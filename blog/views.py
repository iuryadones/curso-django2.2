from django.core.mail import BadHeaderError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ContactForm
from .models import Post
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    html = """
    <html>
      <body>
        <h1>Sejam bem vindos!!!</h1>
      </body>
    </html>
    """
    return HttpResponse(html)

def blog(request):
    template = "blog/blog-index/index.html"
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template, context)

def contact(request):
    template = "blog/blog-contact/form.html"
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['msg']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    context = {'form': form}
    return render(request, template, context)
