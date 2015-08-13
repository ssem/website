import re
import pymongo
from django.http import HttpResponse
from django.shortcuts import render_to_response

def map(request):
    return render_to_response("scanner/map.html")

def search(request):
    f_seek = 0
    search = {}
    # get args
    seek = request.GET.get('seek')
    ip = request.GET.get('ip')
    port = request.GET.get('port')
    country = request.GET.get('country')
    exploit = request.GET.get('exploit')
    protocol = request.GET.get('protocol')
    banner = request.GET.get('banner')
    # filter args
    if seek and len(seek) < 100:
        f_seek = re.search('^\d{1,3}$', seek).group()
    if ip and len(ip) < 100:
        f_ip = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip).group()
        search['ip'] = f_ip
    if port and len(port) < 100:
        f_port = re.search('^\d{1,5}$', port).group()
        search['port'] = f_port
    if country and len(country) < 100:
        f_country = re.search('^\w.*$', country).group()
        search['country'] = f_country.lower()
    if exploit and len(exploit) < 100:
        f_exploit = re.search('^\w.*$', exploit).group()
        search['exploit'] = f_exploit
    if protocol and len(protocol) < 100:
        f_protocol = re.search('^(udp|tcp)$', protocol).group()
        search['protocol'] = f_protocol
    if banner and len(banner) < 100:
        f_banner = banner.lstrip(' ').rstrip(' ')
        search['banner'] = {'$regex': ".*%s.*" % f_banner}
    print search
    # query
    client = pymongo.MongoClient('localhost', 27017)
    db = client['website']
    count = db['scanning'].find(search).count()
    results = list(db['scanning'].find(search, skip=int(f_seek)*20, limit=20))
    # muddle with results before posting
    for result in results:
        if result['port'] == '443':
            result['target_url'] = 'https://%s:%s' % (result['ip'], result['port'])
        else:
            result['target_url'] = 'http://%s:%s' % (result['ip'], result['port'])
        result['banner'] = result['banner'].split('\n')
    return render_to_response("scanner/search.html",
        {'results':results, 'count':count})

def exploit(request):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['website']
    results = db['scanning'].distinct('exploit')
    if results:
        results = results[2:]
    print results
    return render_to_response("scanner/exploit.html",
        {'results':results})
