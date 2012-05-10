# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

# def home(args):
# 	return HttpResponse("Hello")

# def work(args):
# 	return HttpResponse("Goodbye")

# def hello_world(args):
# 	return render_to_response('index.html')
import nltk
from nltk.util import islice
import pylab 
import os


def _create_plot(file, text, words):
	text = list(text) 
	words.reverse() 
	points = [(x,y) for x in range(len(text)) 
					for y in range(len(words)) 
					if text[x].lower() == words[y].lower()]
	if points:
		x,y = zip(*points)
	else:
		x = y = ()
	pylab.figure()
	pylab.plot(x, y, "b|", scalex=.1) 
	pylab.yticks(range(len(words)), words, color="b") 
	pylab.ylim(-1, len(words)) 
	pylab.title("Lexical Dispersion Plot") 
	pylab.xlabel("Word Offset") 
	pylab.savefig('public/graphs/%s_dispersion.png' % file)

def _frequency_plot(file, text): 
	samples = list(islice(text, 25)) 
	 
	cumulative = True 
	freqs = list(text._cumulative_frequencies(samples)) 
	ylabel = "Cumulative Counts" 
	 
	# percents = [f * 100 for f in freqs]  only in ProbDist? 
	 
	pylab.grid(True, color="silver") 

	kwargs = {}
	kwargs["linewidth"] = 2 
	if "title" in kwargs: 
		pylab.title(kwargs["title"]) 
		del kwargs["title"] 
	pylab.figure()
	pylab.plot(freqs, **kwargs) 
	pylab.xticks(range(len(samples)), [str(s) for s in samples], rotation=90) 
	pylab.xlabel("Samples") 
	pylab.ylabel(ylabel) 
	pylab.savefig('public/graphs/%s_frequency.png' % file)

def dispersion(request):
	files = os.listdir('documents')
	for file in files:
		raw = open("documents/%s" % file).read()
		tokens = nltk.word_tokenize(raw)
		text = nltk.Text(tokens)
		_create_plot(file, text,["users", "groups", "ntfs", "permissions"])
		
		raw = open("documents/%s" % file).read()
		tokens = nltk.word_tokenize(raw)
		text = nltk.Text(tokens)
		fdist1 = nltk.FreqDist(text)
		_frequency_plot(file, fdist1)
		
	return render_to_response("index.html", {'chapters' : [1,2,3,4]}, context_instance = RequestContext(request))