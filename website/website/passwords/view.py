import os
import re
from django.http import HttpResponse
from django.shortcuts import render_to_response
from website.passwords.models import Dumps


def hashes(request):
    results = []
    for dump in Dumps.objects.all():
        try:p = round(float(dump.cracked)/float(dump.hash_count) * 100, 2)
        except:p = 0
        try:stat_file = os.path.basename(dump.stat_file)
        except:stat_file=None
        results.append({'name': dump.name,
                        'hashtype': dump.hashtype,
                        'hash_count': dump.hash_count,
                        'cracked': dump.cracked,
                        'hash_file': dump.hash_file,
                        'password_file': dump.password_file,
                        'stat_file': stat_file,
                        'percent': p})
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
    return render_to_response('passwords/password_checker.html')

def password_check_hash(request, hashstring):
    message = []
    for d in Dumps.objects.all():
        for line in open('website/%s' % d.password_file, 'r'):
            if re.search('^%s:' % hashstring, line):
                password = line.split(':')[1]
                message.append('Hash Type: %s' % d.hashtype)
                message.append('Database Leak: %s' % d.name)
                try:percent = float(d.cracked) / float(d.hash_count) * 100
                except:percent = 0
                message.append('Database Cracked: {:.2f}' .format(percent))
                message.append('')
    if len(message) > 1:
        message.insert(0, "")
        message.insert(0, "pick a better password: %s" % password)
        return render_to_response('passwords/password_checker.html',
            {"results": message})
    else:
        return render_to_response('passwords/password_checker.html',
            {"results": ["I have not cracked: %s" % hashstring]})

def password_check_password(request, password):
    message = []
    for d in Dumps.objects.all():
        for line in open('website/%s' % d.password_file, 'r'):
            if re.search(':%s$' % password, line):
                message.append('Hash: %s' % line.split(':')[0])
                message.append('Hash Type: %s' % d.hashtype)
                message.append('Database Leak: %s' % d.name)
                try:percent = float(d.cracked) / float(d.hash_count) * 100
                except:percent = 0
                message.append('Database Cracked: {:.2f}%'.format(percent))
                message.append('')
    if len(message) > 1:
        message.insert(0, "")
        message.insert(0, "pick a better password: %s" % password)
        return render_to_response('passwords/password_checker.html',
            {"results": message})
    else:
        return render_to_response('passwords/password_checker.html',
            {"results": ["I have not cracked: %s" % password]})

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
