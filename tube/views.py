from django.conf import settings
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

import datetime as dt 
from .models import *
from .forms import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import VtubeInfo
from .serializer import InfoSerielizer

from .permissions import IsAdminOrReadOnly

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    videos = Video.objects.all()

    # lastvideo= Video.objects.last()
    # videofile= lastvideo.videofile

    # form= NewVideoForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()
    
    # context = {'videofile':videofile, 'form':form}

    return render(request, 'index.html', {"date":date, "profile":profile, "video":videos})

@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    video = Video.objects.all()

    return render(request, 'profile.html', {"profile": profile, "videos":video})

@login_required(login_url='/accounts/login/')
def video(request,vid=None):
    if vid is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(videos, pk = vid)
    except videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.file_name
    #getting full url - 
    video_url = settings.MEDIA_URL+file_name

    return render(request, "video.html", {"url":video_url})

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

class Infolist(APIView):
    def get(self, request, format=None):
        all_info = VtubeInfo.objects.all()
        serializers = InfoSerializer(all_info, many=True)  
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = InfoSerializer(data = request.data)
        permission_classes = (IsAdminOrReadOnly)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)      

class InfoDescription(APIView):
    permission_classes = (IsAdminOrReadOnly)
    def get_info(self, pk):
        try:
            return VtubeInfo.objects.get(pk=pk)
        except VtubeInfo.DoesNotExist:
            return Http404
            
    def get(self, request, pk, format=None):
        merch = self.get_merch(pk) 
        serializers = MerchSerielizer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        info = self.get_merch(pk)
        serializers = InfoSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        info = self.get_merch(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)