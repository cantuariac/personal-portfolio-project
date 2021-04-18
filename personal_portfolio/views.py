
from django.shortcuts import render
from django.utils.translation import gettext as _
from projects.models import *

profile = Profile(name="Bill Gates", email="bill@contact.com", phone="555-1234",
                  roles="Developer, Data Scientist", about="Bilionaire filantropist")

context = {
    'head_title': 'Portfolio Title',
    'intro_title': _('My Portfolio'),
    'about_title': _('About me'),
    'profile': profile
}


def index(request):
    return render(request, 'index.html', context)


def portfolio_details(request):
    return render(request, 'portfolio-details.html', context)


def blog_single(request):
    return render(request, 'blog-single.html')
