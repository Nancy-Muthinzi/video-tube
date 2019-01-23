from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt 

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render(request, 'welcome.html', {"date":date})

def search_results(request):
    if 'video' in request.GET and request.GET["video"]:
        search_term = request.GET.get("video")
        searched_videos = Video.search_by_video_name(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "videos": searched_videos})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message": message})