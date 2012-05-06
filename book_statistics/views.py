# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

# def home(args):
# 	return HttpResponse("Hello")

# def work(args):
# 	return HttpResponse("Goodbye")

# def hello_world(args):
# 	return render_to_response('index.html')
import nltk
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
	pylab.plot(x, y, "b|", scalex=.1) 
	pylab.yticks(range(len(words)), words, color="b") 
	pylab.ylim(-1, len(words)) 
	pylab.title("Lexical Dispersion Plot") 
	pylab.xlabel("Word Offset") 
	pylab.savefig('public/dispersion.png')

def dispersion(args):
	raw = open("documents/591_16cac_textbook.txt").read()
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	_create_plot(text,["users", "groups", "ntfs", "DNS"])
	return HttpResponse('<img src="static/dispersion.png" />')