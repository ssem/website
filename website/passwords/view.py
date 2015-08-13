import os
import re
import pymongo
from django.http import HttpResponse
from django.shortcuts import render_to_response


def hashes(request):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['website']
    results = list(db['dumps'].find())
    for dump in results:
        try:dump['percent'] = round(float(dump['cracked'])/float(dump['hash_count']) * 100, 2)
        except:dump['percent'] = 0
        try:dump['stat_file'] = os.path.basename(dump['stat_file'])
        except:dump['stat_file'] = "/404.html"
    return render_to_response('passwords/hashes.html',
        {"results": results})

def stats(request, stats_file):
    stats = os.path.join('website/static/stats/', stats_file)
    results = []
    for line in open(stats, 'r'):
        results.append(line.rstrip('\r\n'))
    return render_to_response('passwords/stats.html',
        {'results':results})

def password_checker(request):
    request_type = request.GET.get('type')
    if request_type == 'hash':
        hashstring = request.GET.get('input')
        return _password_check_hash(hashstring)
    elif request_type == 'password':
        password = request.GET.get('input')
        return _password_check_password(password)
    return render_to_response('passwords/password_checker.html')

def _password_check_hash(hashstring):
    results = []
    password = ""
    client = pymongo.MongoClient('localhost', 27017)
    db = client['website']
    for dump in db['dumps'].find():
        result = db[dump['name']].find({'hash': hashstring})
        if result.count() > 0:
            tmp = result[0]['password']
            if len(tmp) > len(password):
                password = tmp
            results.append({'hashstring': hashstring,
                            'hashtype': dump['hashtype'],
                            'dump': dump['name']})
    if len(results) > 0:
        message = "I've cracked: \"%s\"" % password
    else:
        message = "I have NOT cracked: \"%s\"" % hashstring
    return render_to_response('passwords/password_checker.html',
        {"message": message, "results":results})

def _password_check_password(password):
    results = []
    client = pymongo.MongoClient('localhost', 27017)
    db = client['website']
    for dump in db['dumps'].find():
        result = db[dump['name']].find({'password': password})
        if result.count() > 0:
            results.append({'hashstring': result[0]['hash'],
                            'hashtype': dump['hashtype'],
                            'dump': dump['name']})
    if len(results) > 0:
        message = "I've cracked: \"%s\"" % password
    else:
        message = "I have NOT cracked: \"%s\"" % password
    return render_to_response('passwords/password_checker.html',
        {"message": message, "results":results})
