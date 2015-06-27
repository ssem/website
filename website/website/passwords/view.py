from django.http import HttpResponse
from django.shortcuts import render_to_response
from website.passwords.models import Dumps
from website.passwords.models import Passwords

def password_checker(request):
    return render_to_response('passwords/password_checker.html')

def password_check_hash(request, hashstring):
    try:
        p = Passwords.objects.get(hashstring=hashstring)
        if p.password != '':
            return render_to_response('passwords/checker_results.html',
                {'hashstring': p.hashstring,
                 'password': p.password,
                 'dump': p.dump.dump,
                 'hashtype': p.dump.hashtype})
    except:pass
    return HttpResponse('not cracked')

def password_check_password(request, password):
    try:
        p = Passwords.objects.get(password=password)
        return render_to_response('passwords/checker_results.html',
            {'hashstring': p.hashstring,
             'password': p.password,
             'dump': p.dump.dump,
             'hashtype': p.dump.hashtype})
    except:pass
    return HttpResponse('not cracked')

def raw_hashes(request, dump):
    dump = Dumps.objects.filter(dump=dump)
    hashes = Passwords.objects.filter(dump=dump)
    return render_to_response('passwords/raw_hashes.html',
        {'hashes': hashes})

def hashes(request):
    dumps = Dumps.objects.all()
    return render_to_response('passwords/hashes.html',
        {"dumps": dumps})
