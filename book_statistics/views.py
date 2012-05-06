# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(args):
	return HttpResponse("Hello")

def work(args):
	return HttpResponse("Goodbye")

def hello_world(args):
	return render_to_response('index.html')