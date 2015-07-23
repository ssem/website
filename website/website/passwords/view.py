from django.http import HttpResponse
from django.shortcuts import render_to_response
from website.passwords.models import Dumps

def password_checker(request):
    return render_to_response('passwords/password_checker.html')

def password_check_hash(request, hashstring):
    #try:
    #    p = Passwords.objects.get(hashstring=hashstring)
    #    if p.password != '':
    #        return render_to_response('passwords/checker_results.html',
    #            {'hashstring': p.hashstring,
    #             'password': p.password,
    #             'dump': p.dump.dump,
    #             'hashtype': p.dump.hashtype})
    #except:pass
    return render_to_response('passwords/password_checker.html',
        {"no_result": "No Result Found"})

def password_check_password(request, password):
    #try:
    #    p = Passwords.objects.get(password=password)
    #    return render_to_response('passwords/checker_results.html',
    #        {'hashstring': p.hashstring,
    #         'password': p.password,
    #         'dump': p.dump.dump,
    #         'hashtype': p.dump.hashtype})
    #except:pass
    return render_to_response('passwords/password_checker.html',
        {"no_result": "No Result Found"})

def hashes(request):
    results = []
    for dump in Dumps.objects.all():
        try:p = round(float(dump.cracked)/float(dump.hash_count) * 100, 2)
        except:p = 0
        results.append({'name': dump.name,
                        'hashtype': dump.hashtype,
                        'hash_count': dump.hash_count,
                        'cracked': dump.cracked,
                        'percent': p})
    return render_to_response('passwords/hashes.html',
        {"results": results})

def raw_dump(request, dump):
    dump = Dumps.objects.get(dump=dump)
    hashes = Passwords.objects.filter(dump=dump)
    return render_to_response('passwords/raw_hashes.html',
        {'hashes': hashes})

def raw_type(request, hashtype):
    hashes = []
    for dump in Dumps.objects.filter(hashtype=hashtype):
        pass
    return render_to_response('passwords/raw_hashes.html',
        {'hashes': ''})
