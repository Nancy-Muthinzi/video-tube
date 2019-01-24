from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt 
from .models import Video
from .forms import NewVideoForm

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import VtubeMerch
from .serializer import MerchSerielizer

# Create your views here.
def index(request):
    date = dt.date.today()
    videos = Video.objects.all()

    return render(request, 'index.html', {"date":date, "videos":videos})

@login_required(login_url='/accounts/login/')
def video(request, video_id):
        try:
            video = Video.objects.get(id = video_id)
    
        except DoesNotExist:
            raise Http404()
            
        return render(request, "video.html", {"video":video})

@login_required(login_url='/accounts/login/')
def new_video(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.merchant = current_user
            video.save()
        return redirect('index')

    else:
        form = NewVideoForm()
    return render(request, 'new_video.html', {"form": form})        

def search_results(request):
    if 'video' in request.GET and request.GET["video"]:
        search_term = request.GET.get("video")
        searched_videos = Video.search_by_video_name(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "videos": searched_videos})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message": message})

class Merchlist(APIView):
    def get(self, request, format=None):
        all_merch = VtubeMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)  
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)      

