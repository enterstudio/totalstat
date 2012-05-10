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


def _create_plot(text, words):
	text = list(text) 
	words.reverse() 
	points = [(x,y) for x in range(len(text)) 
					for y in range(len(words)) 
					if text[x].lower() == words[y].lower()]
	if points:
		x,y = zip(*points)
	else:
		x = y = ()
	pylab.figure(0)
	pylab.plot(x, y, "b|", scalex=.1) 
	pylab.yticks(range(len(words)), words, color="b") 
	pylab.ylim(-1, len(words)) 
	pylab.title("Lexical Dispersion Plot") 
	pylab.xlabel("Word Offset") 
	pylab.savefig('public/dispersion.png')

def _frequency_plot(text): 
	""" 
	Plot samples from the frequency distribution 
	displaying the most frequent sample first.  If an integer 
	parameter is supplied, stop after this many samples have been 
	plotted.  If two integer parameters m, n are supplied, plot a 
	subset of the samples, beginning with m and stopping at n-1. 
	For a cumulative plot, specify cumulative=True. 
	(Requires Matplotlib to be installed.) 
	@param title: The title for the graph 
	@type title: C{str} 
	@param cumulative: A flag to specify whether the plot is cumulative (default = False) 
	@type title: C{bool} 
	""" 
	try: 
		import pylab 
	except ImportError: 
		raise ValueError('The plot function requires the matplotlib package (aka pylab).' 
					 'See http://matplotlib.sourceforge.net/') 
	 
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
	pylab.figure(1)
	pylab.plot(freqs, **kwargs) 
	pylab.xticks(range(len(samples)), [str(s) for s in samples], rotation=90) 
	pylab.xlabel("Samples") 
	pylab.ylabel(ylabel) 
	pylab.savefig('public/frequency.png')

def dispersion(request):
	raw = open("documents/591_16cac_textbook.txt").read()
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	_create_plot(text,["users", "groups", "ntfs", "permissions"])
	raw = open("documents/591_16cac_textbook.txt").read()
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	fdist1 = nltk.FreqDist(text)
	_frequency_plot(fdist1)
	return render_to_response("index.html", {}, context_instance = RequestContext(request))