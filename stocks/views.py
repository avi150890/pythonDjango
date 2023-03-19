from django.shortcuts import render

# Create your views here.

def home(request):
	import requests 
	import json

	if request.method == 'POST': 
		ticker 	= request.POST['ticker']
		# pk_0f0c4f9431fc4037985b79f0d66ba38e
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/qoute?token=pk_0f0c4f9431fc4037985b79f0d66ba38e")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error.."
		return render(request, 'home.html', {'api':api})

	else:
		return render(request, 'home.html', {'ticker':"Enter a ticker symbol above"})


def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	return render(request, 'add_stock.html', {})