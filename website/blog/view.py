import os
from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    newest = 0
    for f in os.listdir('website/static/blog'):
        if os.path.getmtime(os.path.join('website/static/blog/', f)) > newest:
            newest = f
    blog = os.path.join('website/static/blog/', newest)
    results = []
    for line in open(blog, 'r'):
        results.append(line.rstrip('\r\n'))
    return render_to_response('blog/blog.html',
        {'results':results})

def blog(request, blog):
    stats = os.path.join('website/static/blog/', blog)
    results = []
    for line in open(stats, 'r'):
        results.append(line.rstrip('\r\n'))
    return render_to_response('blog/blog.html',
        {'results':results})
