
from django.shortcuts import render
from django.utils.translation import gettext as _
from projects.models import *

import json
import requests


context = {
    'head_title': 'Portfolio Title',
    'intro_title': _('My Portfolio'),
    'about_title': _('About me')
}


def index(request):
    random_data = json.loads(requests.get(
        "https://randomuser.me/api").text)['results'][0]
    
    random_profile = Profile(name="{} {} {}".format(*random_data['name'].values()),
                             email=random_data['email'],
                             phone=random_data['phone'],
                             picture=random_data['picture']['large'])
    
    context['profile'] = random_profile

    return render(request, 'index.html', context)


def portfolio_details(request):

    return render(request, 'portfolio-details.html', context)


def blog_single(request):
    return render(request, 'blog-single.html')
