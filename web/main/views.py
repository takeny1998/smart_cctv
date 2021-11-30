from django.shortcuts import render
from .models import Event
# Create your views here.
def index(request):
	return render(request, 'main/index.html')


def event_list(request):
	events = reversed(Event.objects.all())

	context = {'events': events}
	return render(request, 'main/event_list.html', context)


def event_play(request, event_id):
	event = Event.objects.get(id=event_id)

	context = {'event': event}
	return render(request, 'main/video_play.html', context)


def streaming(request):
	return render(request, 'main/streaming.html')