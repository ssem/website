from django.http import HttpResponse
from django.shortcuts import render_to_response

def map(request):
    return render_to_response("scanner/map.html")

def search(request):
    return render_to_response("scanner/search.html")

def country(request):
    return redner_to_response("scanner/scan_result.html")

def port(request):
    return redner_to_response("scanner/scan_result.html")
