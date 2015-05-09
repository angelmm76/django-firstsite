from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	home_html = """ <h1>Hello, First site </h1>
		<a href="/blog/">blog</a><br>
		<a href="/polls/">polls</a><br>"""
	return HttpResponse(home_html)
