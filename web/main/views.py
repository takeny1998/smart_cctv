from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def event_list(request):
	return render(request, 'main/event_list.html')

def event_play(request):
	return render(request, 'main/event_list.html')