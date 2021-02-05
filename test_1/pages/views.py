from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "This is about us guys!",
        "my_number" : 99107,
        "my_list" : ['Cabbage','Potato','Eggs','Chicken','Onion']
    }
    return render(request, 'home.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})